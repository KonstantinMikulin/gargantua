from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Row

from handlers.aiogram_dialog_handlers import (
    name_correct_nandler,
    name_error_nandler,
    gender_choose,
    check_dob,
    birthdate_correct_handler,
    birthdate_error_handler
)
from states.fill_account_states import FillAccountSG


# dialog for filling account
fill_account_dialog = Dialog(
    Window(
        Const('Enter your name, please'),
        TextInput(
            id='fill_name',
            on_success=name_correct_nandler,
            on_error=name_error_nandler
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
        Const('Enter you date of birth'),
        TextInput(
            id='fill_birthdate',
            type_factory=check_dob,
            on_success=birthdate_correct_handler,
            on_error=birthdate_error_handler
        ),
        state=FillAccountSG.fill_birthdate
    )
)

