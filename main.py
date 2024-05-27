import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram_dialog import setup_dialogs

from config.config import Config, load_config
from handlers import usesr_handlers
from dialogs.user_dialogs import user_start_dialog

logger = logging.getLogger(__name__)


# info
async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Starting bot')
    
    config: Config = load_config()
    
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    
    dp.include_router(usesr_handlers.router)
    dp.include_router(user_start_dialog)
    setup_dialogs(dp)
    
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())
    