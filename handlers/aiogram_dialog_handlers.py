from time import sleep

from aiogram import Bot, Router
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from config.config import Config
from states.users_dialog_states import DefaultSG, MeasureSG

aiogram_handlers_router = Router()


# handler for processing 'weight' button
async def weight_get_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    await dialog_manager.switch_to(MeasureSG.start_weight)


# handler for processing 'yes' button for account settings
# TODO: ? change logic of this handler
async def account_yes_get_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    await callback.answer('You choose "Yes"') # type: ignore
    await dialog_manager.start(state=DefaultSG.default_dialog, mode=StartMode.RESET_STACK)


# handler for processing 'no' button for account settings
# TODO: change logic of this handler for remind about account
async def account_no_get_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    await callback.answer('You choose "No"') # type: ignore
    await dialog_manager.start(state=DefaultSG.default_dialog, mode=StartMode.RESET_STACK)


# type: pass handler for temporary purpose
async def pass_handler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:
    await message.answer(text=f'We will do something later with {text}')
