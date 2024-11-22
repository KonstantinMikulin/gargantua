from aiogram.types import Message, User, CallbackQuery

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.states import GetLastRecordsSG



async def get_last_measurment(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    if button.widget_id == "get_last_chest":
        await dialog_manager.switch_to(state=GetLastRecordsSG.get_chest, show_mode=ShowMode.EDIT)
    elif button.widget_id == "get_last_waist":
        await dialog_manager.switch_to(state=GetLastRecordsSG.get_waist, show_mode=ShowMode.EDIT)
    elif button.widget_id == "get_last_hips":
        await dialog_manager.switch_to(state=GetLastRecordsSG.get_hips, show_mode=ShowMode.EDIT)
    elif button.widget_id == "get_last_weight":
        await dialog_manager.switch_to(state=GetLastRecordsSG.get_weight, show_mode=ShowMode.EDIT)
