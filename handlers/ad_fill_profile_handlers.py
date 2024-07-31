# aiogram_dialog handlers for fill profile dialog

from datetime import datetime

from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput

from states.users_dialog_states import FillProfileSG, DefaultSG

ad_fill_router = Router()


# TODO: make it DRY
# dialog_handler for processing correct name for filling profile
async def fill_name_correct_nandler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
    ) -> None:
    bot: Bot = dialog_manager.middleware_data['bot']
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    dialog_manager.dialog_data['name'] = message.text
    # TODO: should I delete it after sending or not?
    await message.answer(text=f'Name was saved.\n\nThank you, {text}')
    await dialog_manager.switch_to(state=FillProfileSG.fill_gender, show_mode=ShowMode.DELETE_AND_SEND)


# TODO: make it DRY
# dialog_handler for processing correct name for CHANGING profile
async def change_name_correct_nandler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
    ) -> None:
    bot: Bot = dialog_manager.middleware_data['bot']
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    dialog_manager.dialog_data['name'] = message.text
    
    await message.answer(text=f'Name was changed.\n\nThank you, {text}')
    await dialog_manager.switch_to(state=FillProfileSG.show_profile, show_mode=ShowMode.DELETE_AND_SEND)


# dialog_handler for processing not correct name for filling/changing profile
async def name_error_nandler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, test: str) -> None:
    await message.answer(text='This doesn`t look like a name, bro!')
    

# TODO: make it DRY
# handler for processing gender choose
async def choose_gender(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'fill_m':
        dialog_manager.dialog_data['gender'] = 'male'
        await callback.message.answer(text='Your gender was saved\nThank you')  # type: ignore
        await dialog_manager.switch_to(state=FillProfileSG.fill_birthdate, show_mode=ShowMode.DELETE_AND_SEND)
        
    if callback.data == 'fill_f':
        dialog_manager.dialog_data['gender'] = 'female'
        await callback.message.answer(text='Your gender was saved\nThank you')  # type: ignore
        await dialog_manager.switch_to(state=FillProfileSG.fill_birthdate, show_mode=ShowMode.DELETE_AND_SEND)
      
        
# TODO: make it DRY        
# handler for processing gender CHANGE
async def change_gender(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'change_m':
        dialog_manager.dialog_data['gender'] = 'male'
        await callback.message.answer(text='Your gender was cnahged\nThank you')  # type: ignore
        await dialog_manager.switch_to(state=FillProfileSG.show_profile, show_mode=ShowMode.DELETE_AND_SEND)
        
    if callback.data == 'change_f':
        dialog_manager.dialog_data['gender'] = 'female'
        await callback.message.answer(text='Your gender was changed\nThank you')  # type: ignore
        await dialog_manager.switch_to(state=FillProfileSG.show_profile, show_mode=ShowMode.DELETE_AND_SEND)
        

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

# TODO: make it DRY
# handler for processing FILLING correct date of birth
async def birthdate_fill_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
    ) -> None:
    dob_keys = ['day', 'month', 'year']
    
    bot: Bot = dialog_manager.middleware_data['bot']
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    dob = {k:int(v) for k, v in zip(dob_keys, text.split('.'))}
    dialog_manager.dialog_data['birthdate'] = dob
    
    await message.answer(f'You date of birth is {text}')
    await dialog_manager.switch_to(state=FillProfileSG.fill_init_weight, show_mode=ShowMode.DELETE_AND_SEND)
    

# TODO: make it DRY
# handler for processing CHANGING correct date of birth
async def birthdate_change_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
    ) -> None:
    dob_keys = ['day', 'month', 'year']
    
    bot: Bot = dialog_manager.middleware_data['bot']
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    dob = {k:int(v) for k, v in zip(dob_keys, text.split('.'))}
    dialog_manager.dialog_data['birthdate'] = dob
    
    await message.answer(f'You date of birth is {text}')
    await dialog_manager.switch_to(state=FillProfileSG.show_profile, show_mode=ShowMode.DELETE_AND_SEND)
    
    
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
    weight = round(float(text), 2)
    if 20 <= weight <= 500:
        return text
    
    raise ValueError


# TODO: make it DRY
# handler for processing FILLING correct weight
async def weight_fill_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    bot: Bot = dialog_manager.middleware_data['bot']
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    weight = round(float(text), 2)
    dialog_manager.dialog_data['initial_weight'] = weight
    
    # TODO: add html.escape()
    await message.answer(f'Your current weight is {weight}\nYou will achieve your goals!')
    await dialog_manager.switch_to(state=FillProfileSG.send_photo, show_mode=ShowMode.DELETE_AND_SEND)
    
    
# TODO: make it DRY
# handler for processing CHANGING correct weight
async def weight_change_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    bot: Bot = dialog_manager.middleware_data['bot']
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    weight = round(float(text), 2)
    dialog_manager.dialog_data['initial_weight'] = weight
    
    # TODO: add html.escape()
    await message.answer(f'Your current weight is {weight}\nYou will achieve your goals!')
    await dialog_manager.switch_to(state=FillProfileSG.show_profile, show_mode=ShowMode.DELETE_AND_SEND)
    
    
# handler for processing NOT correct weight
async def weight_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    bot: Bot = dialog_manager.middleware_data['bot']
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    # TODO: change this text
    await message.answer('The weight must be int or float')


# handler for y/n send photo
async def send_initial_photo_handler(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'y_send_photo':
        await dialog_manager.switch_to(state=FillProfileSG.save_photo, show_mode=ShowMode.DELETE_AND_SEND)
    if callback.data == 'n_send_photo':
        bot: Bot = dialog_manager.middleware_data['bot']
        await bot.send_message(chat_id=callback.message.chat.id, text='Thank you')  # type: ignore
        
        await dialog_manager.switch_to(state=FillProfileSG.show_profile, show_mode=ShowMode.DELETE_AND_SEND)


# handler for processing if photo was send
async def save_init_photo(
    message: Message,  
    widget: MessageInput,  
    dialog_manager: DialogManager
    ) -> None:
    # TODO: refactor this line for saving file_unique_id
    dialog_manager.dialog_data['initial_photo'] = message.photo[-1].file_id  # type: ignore
    
    await message.answer('Thank you')
    # TODO: how to automaticly switch dialogs to main menu?
    await dialog_manager.switch_to(state=FillProfileSG.show_profile, show_mode=ShowMode.DELETE_AND_SEND)
    

# TODO: add this logic to 'change_profile' handler    
# handler for processing if photo was send during profile CHANGING
async def save_change_init_photo(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager
    ) -> None:
    await dialog_manager.switch_to(state=FillProfileSG.save_photo, show_mode=ShowMode.DELETE_AND_SEND)


# handler for profile`s data confirmation
async def confirm_profile_data(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'profile_correct':
        # TODO: add functionality for writing down data in temp DB
        await dialog_manager.switch_to(state=FillProfileSG.fill_done, show_mode=ShowMode.SEND)
        
    if callback.data == 'profile_change':
        await dialog_manager.switch_to(state=FillProfileSG.change_profile, show_mode=ShowMode.SEND)
        
# handler for changing name
# TODO: replace 'pass'
async def change_profile(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'name_change':
        await dialog_manager.switch_to(state=FillProfileSG.change_name, show_mode=ShowMode.DELETE_AND_SEND)
    elif callback.data == 'gender_change':
        await dialog_manager.switch_to(state=FillProfileSG.change_gender, show_mode=ShowMode.DELETE_AND_SEND)
    elif callback.data == 'dob_change':
        await dialog_manager.switch_to(state=FillProfileSG.change_dob, show_mode=ShowMode.DELETE_AND_SEND)
    elif callback.data == 'init_weight_change':
        await dialog_manager.switch_to(state=FillProfileSG.change_init_weight, show_mode=ShowMode.DELETE_AND_SEND)
        
        
# handler for proccesing cancel profile filling
async def cancel_fill_profile(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'cancel_fill':
        bot: Bot = dialog_manager.middleware_data['bot']
        
        await bot.send_message(
            chat_id=callback.message.chat.id, # type: ignore
            text='You can use command /profile and fill your profile later'
            )
        await dialog_manager.start(state=DefaultSG.default_dialog, mode=StartMode.RESET_STACK)
