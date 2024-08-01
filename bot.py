import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties 
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram_dialog import setup_dialogs

from config.config import Config, load_config
from keyboards.bot_main_menu import set_main_menu
from handlers.users_handlers import user_router
from handlers.admin_handlers import admin_router
from middlewares.outer_middlewares import UserValidationOuterMiddleware
from lexicon.lexicon import LEXICON_COMMANDS
from dialogs.fill_profile_dialog import fill_profile_dialog
from dialogs.users_dialogs import (
    default_dialog,
    start_dialog,
    what_dialog,
    measure_dialog,
    setup_dialog,
    profile_dialog,
    report_dialog,
    help_dialog,
    desc_dialog,
    support_dialog,
    contacts_dialog
)

logger = logging.getLogger(__name__)


# Some info
async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
                '%(lineno)d - %(name)s - %(message)s'
    )
    
    config: Config = load_config()
    storage = MemoryStorage()
    # redis = Redis(host='localhost')
    # storage = RedisStorage(redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True))
    
    # as default I set HTML for parse mode
    # and set show caption above media
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )
    dp = Dispatcher(storage=storage)
    
    # TODO: remove this after setting DB
    # temp db for user data
    temp_dict: dict[str, str | int | bool] = {'One': 1}
    print(f'Inittial dict: {temp_dict}')
    
    await set_main_menu(bot)
    
    dp.workflow_data.update({'config': config, 'bot': bot, 'temp_dict': temp_dict, 'commands': LEXICON_COMMANDS})
    
    dp.include_routers(admin_router, user_router)
    
    dp.include_routers(
        default_dialog,
        start_dialog,
        what_dialog,
        measure_dialog,
        setup_dialog,
        profile_dialog,
        report_dialog,
        help_dialog,
        desc_dialog,
        support_dialog,
        contacts_dialog,
        fill_profile_dialog
        )
    setup_dialogs(dp)
    
    dp.update.outer_middleware(UserValidationOuterMiddleware())
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())
    