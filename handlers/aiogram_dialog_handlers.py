from datetime import datetime

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput

from states.users_dialog_states import DefaultSG
from states.users_dialog_states import FillAccountSG

aiogram_handlers_router = Router()


# TODO: change logic of this handler for reminding to create account
# general handler for account creation buttons
async def account_create_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'account_yes':
        await callback.answer('You choose "Yes"') # type: ignore
        await dialog_manager.start(state=FillAccountSG.fill_name, show_mode=ShowMode.DELETE_AND_SEND)
    
    if callback.data == 'account_no':
        await callback.answer('You choose "No"') # type: ignore
        # TODO: change start() to done()
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
    await message.answer(text=f'Name was saved.\n\nThank you, {text}')
    await dialog_manager.switch_to(state=FillAccountSG.fill_gender, show_mode=ShowMode.DELETE_AND_SEND)
    

# dialog_handler for processing not correct name for filling account
async def name_error_nandler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, test: str) -> None:
    await message.answer(text='This doesn`t look like a name, bro!')
    
    
# handler for processing gender choose
async def gender_choose(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'fill_m':
        dialog_manager.dialog_data['gender'] = 'male'
        # TODO: remove this line
        print(dialog_manager.dialog_data)
        await callback.message.answer(text='Thank you\nYour gender was saved')  # type: ignore
        await dialog_manager.switch_to(state=FillAccountSG.fill_birthdate, show_mode=ShowMode.DELETE_AND_SEND)
        
    if callback.data == 'fill_f':
        dialog_manager.dialog_data['gender'] = 'female'
        # TODO: remove this line
        print(dialog_manager.dialog_data)
        await callback.message.answer(text='Thank you\nYour gender was saved')  # type: ignore
        await dialog_manager.switch_to(state=FillAccountSG.fill_birthdate, show_mode=ShowMode.DELETE_AND_SEND)
        

# check correct date of birth
def validate_birthdate(text: str) -> str:
    try:
        datetime.strptime(text, "%d.%m.%Y")
    
    except ValueError:
        raise ValueError
    else:
        dob = list(map(int, text.split('.')))
        if all([1 <= dob[0] <= 31, 1 <= dob[1] <= 12, 1924 <= dob[2] <= 2006]):
            return text
        else:
            raise ValueError


# handler for processing correct date of birth
async def birthdate_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
    ) -> None:
    dob_keys = ['day', 'month', 'year']
    
    dob = {k:int(v) for k, v in zip(dob_keys, text.split('.'))}
    dialog_manager.dialog_data['birthdate'] = dob
    # TODO: remove this line
    print(dialog_manager.dialog_data)
    
    await message.answer(f'You date of birth is {text}')
    await dialog_manager.switch_to(state=FillAccountSG.fill_current_weight, show_mode=ShowMode.DELETE_AND_SEND)
    
    
# handler for processing not correct date of birth
async def birthdate_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    error: ValueError
    ) -> None:
    # TODO: change text of this message
    await message.answer('This is not correct date of birth')


# check correct initial weight
def validate_weight(text: str) -> str | None:
        if 20 <= int(text) <= 500:
            return text
        
        raise ValueError


# handler for processing correct weight
async def weight_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    dialog_manager.dialog_data['weight'] = int(text)
    
    await message.answer(f'Your current weight is {text}\nYou will achieve your goals!')
    await dialog_manager.switch_to(state=FillAccountSG.send_photo, show_mode=ShowMode.DELETE_AND_SEND)
    
    
# handler for processing NOT correct weight
async def weight_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    # TODO: change this text
    await message.answer('Enter correct weight, please')


# handler for y/n send photo
# async def send_photo_handler(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
#     if callback.data == 'yes_send_photo':
        


# handler for processing if photo was send
async def save_photo_handler(
    message: Message,  
    widget: MessageInput,  
    dialog_manager: DialogManager
    ) -> None:
    # TODO: refactor this line for saving file_unique_id
    dialog_manager.dialog_data['initial_photo'] = message.photo[-1].file_id  # type: ignore
    print(dialog_manager.dialog_data)
    
    await message.answer('Thank you')
    await dialog_manager.switch_to(state=FillAccountSG.fill_done, show_mode=ShowMode.DELETE_AND_SEND)


# type: pass handler for temporary purpose
async def pass_handler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:
    await message.answer(text=f'We will do something later with {text}')
