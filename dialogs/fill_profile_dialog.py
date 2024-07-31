from aiogram.enums import ContentType

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button, Row, Column
from aiogram_dialog.widgets.media import DynamicMedia

from handlers.ad_fill_profile_handlers import (
    fill_name_correct_nandler,
    name_error_nandler,
    change_name_correct_nandler,
    choose_gender,
    change_gender,
    validate_birthdate,
    birthdate_fill_correct_handler,
    birthdate_change_correct_handler,
    birthdate_error_handler,
    validate_weight,
    weight_fill_correct_handler,
    weight_change_correct_handler,
    weight_error_handler,
    send_initial_photo_handler,
    save_init_photo,
    save_change_init_photo,
    confirm_profile_data,
    change_profile,
    cancel_fill_profile
)

from states.users_dialog_states import FillProfileSG
from getters.aiogram_dialog_getters import get_profile_data, get_init_photo

# TODO: add cancel button
# TODO: make some text in these dialog bold
# TODO: decrease number of 'Thank you', please

# dialog for filling profile
fill_profile_dialog = Dialog(
    Window(
        Const('Enter your name, please'),
        TextInput(
            id='fill_name',
            on_success=fill_name_correct_nandler,
            on_error=name_error_nandler  # type: ignore
            ),
        Button(
            Const('Cancel'),
            id='cancel_fill',
            on_click=cancel_fill_profile
        ),
        state=FillProfileSG.fill_name
    ),
    Window(
        Const('Enter your gender, please'),
        Row(
            Button(
                text=Const('Male'),
                id='fill_m',
                on_click=choose_gender
            ),
            Button(
                text=Const('Female'),
                id='fill_f',
                on_click=choose_gender
            )
        ),
        Button(
            Const('Cancel'),
            id='cancel_fill',
            on_click=cancel_fill_profile
        ),
        state=FillProfileSG.fill_gender
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
            on_success=birthdate_fill_correct_handler,
            on_error=birthdate_error_handler
        ),
        Button(
            Const('Cancel'),
            id='cancel_fill',
            on_click=cancel_fill_profile
        ),
        state=FillProfileSG.fill_birthdate
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
            on_success=weight_fill_correct_handler,  # type: ignore
            on_error=weight_error_handler  # type: ignore
        ),
        Button(
            Const('Cancel'),
            id='cancel_fill',
            on_click=cancel_fill_profile
        ),
        state=FillProfileSG.fill_init_weight
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
        Button(
            Const('Cancel'),
            id='cancel_fill',
            on_click=cancel_fill_profile
        ),
        state=FillProfileSG.send_photo
    ),
    Window(
        Const('Download you first photo, please'),
        MessageInput(
            func=save_init_photo,
            content_types=ContentType.PHOTO
        ),
        Button(
            Const('Cancel'),
            id='cancel_fill',
            on_click=cancel_fill_profile
        ),
        state=FillProfileSG.save_photo
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
        Format('Date of birth: {date_of_birth}'),
        Format('Initial weight is {initial_weight}\n'),
        Column(
            Button(
                text=Const('It is fine'),
                id='profile_correct',
                on_click=confirm_profile_data
            ),
            Button(
                text=Const('Let`s change some'),
                id='profile_change',
                on_click=confirm_profile_data
            )
            ),
        getter=get_profile_data,
        state=FillProfileSG.show_profile
    ),
    Window(
        Const('Your profile was saved'),
        state=FillProfileSG.fill_done
    ),
    Window(
        # TODO: should I delete text of this window after choosing button?
        Const('What do you want to change?'),
        # TODO: refactor buttons placement if needed
        Column(
            Button(
                Const('Name'),
                id='name_change',
                on_click=change_profile
            ),
            Button(
                Const('Gender'),
                id='gender_change',
                on_click=change_profile
            ),
            Button(
                Const('Date of birth'),
                id='dob_change',
                on_click=change_profile
            ),
            Button(
                Const('Initial weight'),
                id='init_weight_change',
                on_click=change_profile
            ),
            # button to add photo if there is no initial photo
            Button(
                Const('Add first photo'),
                id='add_init_photo',
                on_click=change_profile,
                when='no_photo'
            ),
            # button to change initial photo
            Button(
                Const('Change initial photo'),
                id='change_init_photo',
                on_click=change_profile,
                when='initial_photo'
            ),
            Button(
                text=Const('It is fine'),
                id='profile_correct',
                on_click=confirm_profile_data
            )
        ),
        state=FillProfileSG.change_profile,
        getter=get_init_photo # type: ignore
    ),
    # window for changing name in profile
    Window(
        Const('Enter your name, please'),
        TextInput(
            id='change_name',
            on_success=change_name_correct_nandler,
            on_error=name_error_nandler # type: ignore
        ),
        state=FillProfileSG.change_name
    ),
    # window for changing gender
    Window(
        Const('Choose your gender'),
        Row(
            Button(
                text=Const('Male'),
                id='change_m',
                on_click=change_gender
            ),
            Button(
                text=Const('Female'),
                id='change_f',
                on_click=change_gender
            )
        ),
        state=FillProfileSG.change_gender
    ),
    # window for changing dob
    Window(
        Const(
            'Enter new date of birth\n\n'
            'Use this format: DD.MM.YY\n\n'
            '01.12.2012 for example'
            ),
        TextInput(
            id='change_dob',
            type_factory=validate_birthdate,
            on_success=birthdate_change_correct_handler,
            on_error=birthdate_error_handler
        ),
        state=FillProfileSG.change_dob
    ),
    # window for changing initial weight
    Window(
        Const(
            'Enter you correct current weight in kg, please\n\n'
            'Enter just kg, 75 for example\n'
            'Or enter kg and gr if you want\n'
            'Like that: 75.45\n\n'
            'We will use this data for future analytics'
            ),
        TextInput(
            id='change_weight',
            type_factory=validate_weight,
            on_success=weight_change_correct_handler,  # type: ignore
            on_error=weight_error_handler  # type: ignore
        ),
        state=FillProfileSG.change_init_weight
    )
)
