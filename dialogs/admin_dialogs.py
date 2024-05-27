from aiogram.fsm.state import State, StatesGroup
from aiogram.types import User

from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.text import Const, Format


# states for admin
class AdminSG(StatesGroup):
    start_dialog = State()
    

# getting any usefull admin`s` data
async def get_admin_data(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict[str, str]:
    admin_data = {
        'admin_name': event_from_user.username
    }
    
    return admin_data


admin_start_dialog = Dialog(
    Window(
        Format('Hello, admin {admin_name}'),
        getter=get_admin_data,
        state=AdminSG.start_dialog
    )
)
