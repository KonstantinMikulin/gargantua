from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from dialogs.user_dialogs import UserSG

router = Router()


@router.message(CommandStart())
async def process_cmd_start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=UserSG.start_dialog, mode=StartMode.RESET_STACK)
