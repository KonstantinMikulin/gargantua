import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties 
from aiogram.enums import ParseMode

from aiogram_dialog import setup_dialogs

from config.config import Config, load_config
from keyboards.bot_main_menu import set_main_menu
from handlers.users_handlers import user_handlers_router
from middlewares.outer_middlewares import (
    UserValidationOuterMiddleware,
    CommandsValidationOuterMiddleware
)
from lexicon.lexicon import LEXICON_COMMANDS
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
        format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
                '%(lineno)d - %(name)s - %(message)s'
    )
    
    config: Config = load_config()
    
    # as default I set Markdown for parse mode
    # and set show caption above media
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            show_caption_above_media=True
        )
    )
    dp = Dispatcher()
    
    await set_main_menu(bot)
    
    dp.workflow_data.update({'config': config, 'bot': bot, 'commands': LEXICON_COMMANDS})
    
    dp.include_router(user_handlers_router)
    
    dp.include_routers(
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
    setup_dialogs(dp)
    
    dp.update.outer_middleware(UserValidationOuterMiddleware())
    dp.update.outer_middleware(CommandsValidationOuterMiddleware())
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())
    