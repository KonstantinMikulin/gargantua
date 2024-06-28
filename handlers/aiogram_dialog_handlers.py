from pprint import pprint

from aiogram import Bot, Router
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from config.config import Config
from states.users_dialog_states import DefaultSG, MeasureSG

aiogram_handlers_router = Router()


# TODO: change logic of this handler for reminding to create account
# genaral handler for account creation buttons
async def account_create_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'account_yes':
        await callback.answer('You choose "Yes"') # type: ignore
        await dialog_manager.start(state=DefaultSG.default_dialog, mode=StartMode.RESET_STACK, show_mode=ShowMode.DELETE_AND_SEND)
    
    if callback.data == 'account_no':
        await callback.answer('You choose "No"') # type: ignore
        await dialog_manager.start(state=DefaultSG.default_dialog, mode=StartMode.RESET_STACK, show_mode=ShowMode.DELETE_AND_SEND)


# type: pass handler for temporary purpose
async def pass_handler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:
    await message.answer(text=f'We will do something later with {text}')
