from typing import Any

from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager, Data
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.states import AddWeightSG


# handler for cancel button
async def cancel_btn_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    await callback.message.edit_text("Отменено") # type:ignore


# TODO: remove this handler
async def okey_clicked(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    pass
