from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.states import GetLastRecordsSG, GetAllRecordsSG


# get one last measurment record
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


# get all measurments records
async def get_all_measurments(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    if button.widget_id == "get_all_chest":
        await dialog_manager.switch_to(state=GetAllRecordsSG.get_all_chest, show_mode=ShowMode.EDIT)
    elif button.widget_id == "get_all_waist":
        await dialog_manager.switch_to(state=GetAllRecordsSG.get_all_waist, show_mode=ShowMode.EDIT)
    elif button.widget_id == "get_all_hips":
        await dialog_manager.switch_to(state=GetAllRecordsSG.get_all_hips, show_mode=ShowMode.EDIT)
    elif button.widget_id == "get_all_weights":
        await dialog_manager.switch_to(state=GetAllRecordsSG.get_all_weights, show_mode=ShowMode.EDIT)
