from aiogram.enums import ContentType

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format, Multi
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.media import DynamicMedia

from handlers.aiogram_dialog_handlers import (
    name_correct_nandler,
    name_error_nandler,
    gender_choose,
    validate_birthdate,
    birthdate_correct_handler,
    birthdate_error_handler,
    validate_weight,
    weight_correct_handler,
    weight_error_handler,
    photo_send_handler
)
from states.users_dialog_states import FillAccountSG
from getters.aiogram_dialog_getters import get_profile_data


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
                id='fill_male',
                on_click=gender_choose
            ),
            Button(
                text=Const('Female'),
                id='fill_female',
                on_click=gender_choose
            )
        ),
        state=FillAccountSG.fill_gender
    ),
    Window(
        # TODO: change text of this message
        Const('Enter you date of birth'),
        TextInput(
            id='fill_birthdate',
            type_factory=validate_birthdate,
            on_success=birthdate_correct_handler,
            on_error=birthdate_error_handler
        ),
        state=FillAccountSG.fill_birthdate
    ),
    Window(
        # TODO: change text of this message
        Const('Enter you current weight, please'),
        TextInput(
            id='fill_initial_weight',
            type_factory=validate_weight,
            on_success=weight_correct_handler,  # type: ignore
            on_error=weight_error_handler  # type: ignore
        ),
        state=FillAccountSG.fill_current_weight
    ),
    Window(
        Const('Do you want to send photo?'),
        MessageInput(
            func=photo_send_handler,
            content_types=ContentType.PHOTO
        ),
        state=FillAccountSG.send_photo
    ),
    Window(
        Const('Here are your profile:'),
        Format('Name: {name}'),
        Format('Gender: {gender}'),
        Const('\nThis is your initial photo:'),
        DynamicMedia('initial_photo'),
        getter=get_profile_data,
        state=FillAccountSG.fill_done
    )
)
