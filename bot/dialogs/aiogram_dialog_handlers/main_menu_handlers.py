from aiogram.types import Message, CallbackQuery, User

from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from bot.db import add_weight, get_last_weight

from bot.dialogs import AddWeightSG, AddMeasurmentsSG


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
