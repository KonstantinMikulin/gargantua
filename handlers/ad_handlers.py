# aiogram_dialog handlers

from aiogram import Router
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from states.users_dialog_states import DefaultSG
from states.users_dialog_states import FillprofileSG

ad_handlers_router = Router()


# TODO: change logic of this handler for reminding to create profile
# general handler for profile creation buttons
async def profile_create_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'profile_yes':
        await callback.answer('You choose "Yes"') # type: ignore
        await dialog_manager.start(state=FillprofileSG.fill_name, show_mode=ShowMode.DELETE_AND_SEND)
    
    if callback.data == 'profile_no':
        await callback.answer('You choose "No"') # type: ignore
        # TODO: change start() to done()
        await dialog_manager.start(state=DefaultSG.default_dialog, mode=StartMode.RESET_STACK, show_mode=ShowMode.DELETE_AND_SEND)


# type: pass handler for temporary purpose
async def pass_handler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:
    await message.answer(text=f'We will do something later with {text}')
