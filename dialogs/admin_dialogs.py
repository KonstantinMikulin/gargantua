from aiogram.fsm.state import State, StatesGroup
from aiogram.types import User

from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.text import Format


class AdminSG(StatesGroup):
    start_dialog = State()
    
    
async def get_username(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict[str, str]:
    return {'username': event_from_user.username}


admin_start_dialog = Dialog(
    Window(
        Format('Hello {username}'),
        getter=get_username,
        state=AdminSG.start_dialog
    ),
)
