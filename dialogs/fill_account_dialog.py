from aiogram.enums import ContentType

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button, Row, Column
from aiogram_dialog.widgets.media import DynamicMedia

from handlers.ad_fill_account_handlers import (
    name_correct_nandler,
    name_error_nandler,
    gender_choose,
    validate_birthdate,
    birthdate_correct_handler,
    birthdate_error_handler,
    validate_weight,
    weight_correct_handler,
    weight_error_handler,
    send_initial_photo_handler,
    save_initial_photo_handler,
    confirm_account_data,
    change_account
)
from states.users_dialog_states import FillAccountSG
from getters.aiogram_dialog_getters import get_profile_data

# TODO: make some text in these dialog bold
# TODO: decrease number of 'Thank you', please

# dialog for filling account
fill_account_dialog = Dialog(
    Window(
        Const('Enter your name, please'),
        TextInput(
            id='fill_name',
            on_success=name_correct_nandler,
            on_error=name_error_nandler  # type: ignore
            ),
        state=FillAccountSG.fill_name
    ),
    Window(
        Const('Enter your gender, please'),
        Row(
            Button(
                text=Const('Male'),
                id='fill_m',
                on_click=gender_choose
            ),
            Button(
                text=Const('Female'),
                id='fill_f',
                on_click=gender_choose
            )
        ),
        state=FillAccountSG.fill_gender
    ),
    Window(
        Const(
            'Enter you date of birth\n'
            'Use this format: DD.MM.YY\n\n'
            '01.12.2012 for example'
            ),
        TextInput(
            id='fill_dob',
            type_factory=validate_birthdate,
            on_success=birthdate_correct_handler,
            on_error=birthdate_error_handler
        ),
        state=FillAccountSG.fill_birthdate
    ),
    Window(
        Const(
            'Enter you current weight in kg, please\n\n'
            'Enter just kg, 75 for example\n'
            'Or enter kg and gr if you want\n'
            'Like that: 75.45\n\n'
            'We will use this data for future analytics'
            ),
        TextInput(
            id='fill_weight',
            type_factory=validate_weight,
            on_success=weight_correct_handler,  # type: ignore
            on_error=weight_error_handler  # type: ignore
        ),
        state=FillAccountSG.fill_current_weight
    ),
    Window(
        Const('Do you want to send photo?'),
        Button(
            Const('Yes'),
            id = 'y_send_photo',
            on_click=send_initial_photo_handler
        ),
        Button(
            Const('No'),
            id='n_send_photo',
            on_click=send_initial_photo_handler
        ),
        state=FillAccountSG.send_photo
    ),
    Window(
        Const('Download you first photo, please'),
        MessageInput(
            func=save_initial_photo_handler,
            content_types=ContentType.PHOTO
        ),
        state=FillAccountSG.save_photo
    ),
    Window(
        Const(
            text='This is your initial photo\n',
            when='initial_photo'
            ),
        DynamicMedia(
            selector='initial_photo',
            when='initial_photo'
            ),
        Const('Here is your profile:\n'),
        Format('Name: {name}'),
        Format('Gender: {gender}'),
        Format('Initial weight is {initial_weight}\n'),
        Column(
            Button(
                text=Const('It is fine'),
                id='acc_correct',
                on_click=confirm_account_data
            ),
            Button(
                text=Const('Let`s change some'),
                id='acc_change',
                on_click=confirm_account_data
            )
            ),
        getter=get_profile_data,
        state=FillAccountSG.show_account
    ),
    Window(
        Const('What do you want to change?'),
        # TODO: refactor buttons placement if needed
        Column(
            Button(
                Const('Name'),
                id='name_change',
                on_click=change_account
            ),
            Button(
                Const('Gender'),
                id='gender_change',
                on_click=change_account
            ),
            Button(
                Const('Date of birth'),
                id='dob_change',
                on_click=change_account
            ),
            Button(
                Const('Initial weight'),
                id='init_weight_change',
                on_click=change_account
            )
        ),
        state=FillAccountSG.change_account
    )
)
