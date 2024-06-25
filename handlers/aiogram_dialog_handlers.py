from aiogram import Bot, Router
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from config.config import Config

aiogram_handlers_router = Router()


# handler for processing 'yes' button for account settings
# TODO: change logic of this handler
async def account_yes_get_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    await callback.message.answer('You choose "Yes"') # type: ignore
    # TODO: remove this line after writing logic for creating account 
    await dialog_manager.reset_stack()


# handler for processing 'no' button for account settings
# TODO: change logic of this handler for remind about account
async def account_no_get_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    await callback.message.answer('You choose "No"') # type: ignore
    await dialog_manager.reset_stack()
    


# type: pass handler for temporary purpose
async def pass_handler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:
    await message.answer(text=f'We will do something later with {text}')
