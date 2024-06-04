import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram_dialog import setup_dialogs

from config.config import Config, load_config
from keyboards.bot_main_menu import set_main_menu
from handlers import users_handlers
# TODO: refactor this (maybe import list with dialogs from mudule)
from dialogs.users_dialogs import (
    start_dialog,
    what_dialog,
    measure_dialog,
    setup_dialog,
    account_dialog,
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
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Starting bot')
    
    config: Config = load_config()
    
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    
    await set_main_menu(bot)
    
    dp.workflow_data.update({'config': config, 'my_bot': bot})
    dp.include_router(users_handlers.user_handlers_router)
    # TODO: check that this method work correctly after refactoring import of dialogs
    dp.include_routers(
        *[
        start_dialog,
        what_dialog,
        measure_dialog,
        setup_dialog,
        account_dialog,
        report_dialog,
        help_dialog,
        desc_dialog,
        support_dialog,
        contacts_dialog
        ]
        )
    setup_dialogs(dp)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())
    