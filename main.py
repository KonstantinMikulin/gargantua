import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram_dialog import setup_dialogs

from config.config import Config, load_config
from handlers import admin_handlers
from dialogs.admin_dialogs import admin_start_dialog

logger = logging.getLogger(__name__)


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
    
<<<<<<< HEAD
    dp.include_router(admin_start_dialog)
    setup_dialogs(dp)
    
=======
    dp.include_router(admin_handlers.router)
    dp.include_router(admin_start_dialog)
    setup_dialogs(dp)
>>>>>>> 5292fba (addde main.py with one simple /start cmd)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())
    