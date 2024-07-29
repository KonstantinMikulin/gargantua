# aiogram_dialog handlers for fill account dialog

from datetime import datetime

from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput

from states.users_dialog_states import FillAccountSG, ChangeAccountSG

ad_fill_router = Router()


# dialog_handler for processing correct name for filling account
async def name_correct_nandler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
    ) -> None:
    bot: Bot = dialog_manager.middleware_data['bot']
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    dialog_manager.dialog_data['name'] = message.text
    print(dialog_manager.dialog_data)
    
    widget_id = dialog_manager.middleware_data.get('aiogd_context').widget_data.keys() # type: ignore
    
    if list(widget_id)[0] == 'fill_name':
        # TODO: should I delete it after sending or not?
        await message.answer(text=f'Name was saved.\n\nThank you, {text}')
        await dialog_manager.switch_to(state=FillAccountSG.fill_gender, show_mode=ShowMode.DELETE_AND_SEND)
    
    # TODO: fix this lines
    if list(widget_id)[0] == 'change_name':
        await message.answer(text=f'Name was changed.\n\nThank you, {text}')
        await dialog_manager.start(
            state=FillAccountSG.show_account,
            mode=StartMode.NORMAL,
            show_mode=ShowMode.DELETE_AND_SEND
            )
    

# dialog_handler for processing not correct name for filling account
async def name_error_nandler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, test: str) -> None:
    await message.answer(text='This doesn`t look like a name, bro!')
    

# handler for processing gender choose
async def gender_choose(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'fill_m':
        dialog_manager.dialog_data['gender'] = 'male'
        await callback.message.answer(text='Your gender was saved\nThank you')  # type: ignore
        await dialog_manager.switch_to(state=FillAccountSG.fill_birthdate, show_mode=ShowMode.DELETE_AND_SEND)
        
    if callback.data == 'fill_f':
        dialog_manager.dialog_data['gender'] = 'female'
        await callback.message.answer(text='Your gender was saved\nThank you')  # type: ignore
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
    
    bot: Bot = dialog_manager.middleware_data['bot']
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    dob = {k:int(v) for k, v in zip(dob_keys, text.split('.'))}
    dialog_manager.dialog_data['birthdate'] = dob
    
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
    weight = round(float(text), 2)
    if 20 <= weight <= 500:
        return text
    
    raise ValueError


# handler for processing correct weight
async def weight_correct_handler(
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
    await dialog_manager.switch_to(state=FillAccountSG.send_photo, show_mode=ShowMode.DELETE_AND_SEND)
    
    
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
        await dialog_manager.switch_to(state=FillAccountSG.save_photo, show_mode=ShowMode.DELETE_AND_SEND)
    if callback.data == 'n_send_photo':
        bot: Bot = dialog_manager.middleware_data['bot']
        await bot.send_message(chat_id=callback.message.chat.id, text='Thank you')  # type: ignore
        
        await dialog_manager.switch_to(state=FillAccountSG.show_account, show_mode=ShowMode.DELETE_AND_SEND)


# handler for processing if photo was send
async def save_initial_photo_handler(
    message: Message,  
    widget: MessageInput,  
    dialog_manager: DialogManager
    ) -> None:
    # TODO: refactor this line for saving file_unique_id
    dialog_manager.dialog_data['initial_photo'] = message.photo[-1].file_id  # type: ignore
    
    await message.answer('Thank you')
    # TODO: how to automaticly switch dialogs to main menu?
    await dialog_manager.switch_to(state=FillAccountSG.show_account, show_mode=ShowMode.DELETE_AND_SEND)


# handler for account`s data confirmation
async def confirm_account_data(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'acc_correct':
        await dialog_manager.switch_to(state=FillAccountSG.fill_done, show_mode=ShowMode.SEND)
        
    if callback.data == 'acc_change':
        await dialog_manager.switch_to(state=FillAccountSG.change_account, show_mode=ShowMode.SEND)
        
        
# handler for changing name
# TODO: replace 'pass'
async def change_account(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    if callback.data == 'name_change':
        await dialog_manager.start(
            state=ChangeAccountSG.change_name,
            mode=StartMode.NORMAL,
            show_mode=ShowMode.DELETE_AND_SEND
            )
    elif callback.data == 'gender_change':
        pass
    elif callback.data == 'dob_change':
        pass
    elif callback.data == 'init_weight_change':
        pass
