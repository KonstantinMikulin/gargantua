import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import Redis, RedisStorage

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.config_reader import get_config, BotConfig, DbConfig, RedisConfig
from bot.handlers import get_commands_routers
from bot.handlers.main_bot_menu import set_main_menu
from bot.db import Base
from bot.middlewares import DbSessionMiddleware, TrackAllUsersMiddleware


# main func
async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] #%(levelname)-8s %(filename)s:"
        "%(lineno)d - %(name)s - %(message)s",
    )

    logger = logging.getLogger(__name__)
    logger.info("Bot starts")

    # creating bot`s config 'object'
    bot_config = get_config(BotConfig, "bot")

    # create database config 'object'
    db_config = get_config(DbConfig, "db")
    
    # creating redis config
    redis_config = get_config(RedisConfig, "redis")

    # create sqlachemy engine
    engine = create_async_engine(url=str(db_config.dsn), echo=db_config.is_echo)

    # open new connection with database
    async with engine.begin() as conn:
        # simple text query
        await conn.execute(text("SELECT 1"))

    # create tables
    async with engine.begin() as connection:
        # await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

    redis = Redis(
        host=redis_config.host,
        port=redis_config.port,
        db=redis_config.db,
        username=redis_config.username,
        password=redis_config.password
    )
    
    # Инициализируем хранилище (создаем экземпляр класса RedisStorage)
    storage = RedisStorage(redis=redis)

    # creating dispatcher object
    dp = Dispatcher(
        admin_id=bot_config.admin_id,
        # db_engine=engine,
        storage=storage
    )

    # creating bot object
    bot = Bot(
        token=bot_config.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    # connecting handlers`routers
    dp.include_routers(*get_commands_routers())

    # registering middlewares
    Sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    dp.update.outer_middleware(DbSessionMiddleware(Sessionmaker))
    dp.message.outer_middleware(TrackAllUsersMiddleware())

    # set main menu
    await set_main_menu(bot)

    # skip updates and run pulling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
