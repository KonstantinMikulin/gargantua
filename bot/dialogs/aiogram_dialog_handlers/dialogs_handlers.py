from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.states import MainMenuSG


# TODO: check and remove this fucntion
# handler for cancel button
async def cancel_btn_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    await callback.message.edit_text("Отменено") # type:ignore


# TODO: check and remove this fucntion
async def okey_clicked(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(
        state=MainMenuSG.main_state,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.DELETE_AND_SEND
    )
