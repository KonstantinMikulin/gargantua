from aiogram.types import Message, User, CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button



async def get_last_measurment(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    if button.widget_id == "get_last_chest":
        