from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs import AddWeightSG, AddMeasurmentsSG, GetLastRecordsSG


# main menu weight`s button clicked
async def weight_main_btn(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    await dialog_manager.start(
        state=AddWeightSG.add_weight,
        mode=StartMode.NORMAL,
        show_mode=ShowMode.DELETE_AND_SEND
        )


# main menu measurements` button clicked
async def measure_main_btn(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(
        state=AddMeasurmentsSG.add_chest,
        mode=StartMode.NORMAL,
        show_mode=ShowMode.DELETE_AND_SEND,
    )


# main menu last measurements` button clicked
async def last_main_btn(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(
        state=GetLastRecordsSG.choose,
        mode=StartMode.NORMAL,
        show_mode=ShowMode.DELETE_AND_SEND,
    )
