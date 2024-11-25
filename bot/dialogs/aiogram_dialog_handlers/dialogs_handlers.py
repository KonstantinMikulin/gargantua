from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


# handler for cancel button
async def cancel_btn_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    await callback.message.edit_text("Действие отменено") # type:ignore
    await dialog_manager.reset_stack()
