from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from dialogs.admin_dialogs import AdminSG

router = Router()


@router.message(CommandStart())
async def process_cmd_start_admin(message: Message, dialog_manager: DialogManager) -> None:
<<<<<<< HEAD
    await dialog_manager.start(state=AdminSG.start_dialog, mode=StartMode.RESET_STACK)
=======
    await dialog_manager.start(
        state=AdminSG.start_dialog,
        mode=StartMode.RESET_STACK
    )
>>>>>>> 5292fba (addde main.py with one simple /start cmd)
