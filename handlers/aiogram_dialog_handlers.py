from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from states.users_dialog_states import DefaultSG
from states.fill_account_states import FillAccountSG

aiogram_handlers_router = Router()


# TODO: change logic of this handler for reminding to create account
# genaral handler for account creation buttons
async def account_create_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'account_yes':
        await callback.answer('You choose "Yes"') # type: ignore
        await dialog_manager.start(state=FillAccountSG.fill_name, show_mode=ShowMode.DELETE_AND_SEND)
    
    if callback.data == 'account_no':
        await callback.answer('You choose "No"') # type: ignore
        await dialog_manager.start(state=DefaultSG.default_dialog, mode=StartMode.RESET_STACK, show_mode=ShowMode.DELETE_AND_SEND)


# dialog_handler for processing correct name for filling account
async def name_correct_nandler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
    ) -> None:
    dialog_manager.dialog_data['name'] = message.text
    # TODO: remove this line
    print(dialog_manager.dialog_data)
    # TODO: should I delete it after sending or not?
    await message.answer(text=f'Name is saved.\n\nThank you, {text}')
    await dialog_manager.switch_to(state=FillAccountSG.fill_gender, show_mode=ShowMode.DELETE_AND_SEND)
    

# dialog_handler for processing not correct name for filling account
async def name_error_nandler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager) -> None:
    await message.answer(text='This doesn`t look like a name, bro!')
    
    
# handler for processing gender choose
async def gender_choose(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'fill_male':
        dialog_manager.dialog_data['gender'] = 'male'
        # TODO: remove this line
        print(dialog_manager.dialog_data)
        await callback.message.answer(text='Thank you')
        # await dialog_manager.switch_to(state=FillAccountSG.fill_birthdate, show_mode=ShowMode.DELETE_AND_SEND)
        
    if callback.data == 'fill_female':
        dialog_manager.dialog_data['gender'] = 'female'
        # TODO: remove this line
        print(dialog_manager.dialog_data)
        await callback.message.answer(text='Thank you')
        # await dialog_manager.switch_to(state=FillAccountSG.fill_birthdate, show_mode=ShowMode.DELETE_AND_SEND)


# type: pass handler for temporary purpose
async def pass_handler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:
    await message.answer(text=f'We will do something later with {text}')
