from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


# handler for processing 'yes' button for account settings
# TODO: change logic of this handler
async def account_yes_get_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    await callback.message.answer('You choose "Yes"') # type: ignore


# handler for processing 'no' button for account settings
# TODO: change logic of this handler
async def account_no_get_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    await callback.message.answer('You choose "No"') # type: ignore
