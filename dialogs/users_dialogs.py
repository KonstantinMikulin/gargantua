from aiogram.types import User

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Row, Url
from getters.aiogram_dialog_getters import get_username

from lexicon.lexicon import LEXICON_RU
from handlers.aiogram_dialog_handlers import (
    account_create_click,
    name_correct_nandler,
    name_error_nandler,
    gender_choose
)
from states.users_dialog_states import (
    DefaultSG,
    StartSG,
    HelpSG,
    DescSG,
    WhatSG,
    MeasureSG,
    SetupSG,
    AccountSG,
    ReportSG,
    SupportSG,
    ContactsSG
)

# TODO: refactor 'main menu' with inline keyboard
# dialog for main keyboard menu
default_dialog = Dialog(
    Window(
        Const(text='Main menu'),
        # TODO: set on_click
        Button(text=Const('Weight'), id='weight', on_click=None),
        Button(text=Const('Measure'), id='measure', on_click=None),
        state=DefaultSG.default_dialog
    )
)

# TODO: add nessesary Windows
start_dialog = Dialog(
    Window(
        Format(LEXICON_RU['/start']),
        Row(
            Button(text=Const('Yes'), id='account_yes', on_click=account_create_click),
            Button(Const('No'), id='account_no', on_click=account_create_click),
            
        ),
        getter=get_username,
        state=StartSG.start_dialog
    )
)

# /help dialog
# TODO: add nessesary Windows
help_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/help']),
        state=HelpSG.start_help,
        # TODO: uncomment getter`s row
        # getter=get_commands
    )
)

# /desc dialog
# TODO: add nessesary Windows
desc_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/desc']),
        state=DescSG.start_desc
    )
)

# TODO: add nessesary Windows
what_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/what']),
        Url(
            text=Const('Open'),
            url=Const('https://clck.ru/3BUGPY'),
            id='gargantua_link'
        ),
        state=WhatSG.start_what
    )
)

# TODO: add nessesary Windows
measure_dialog = Dialog(
    Window(
        Format(LEXICON_RU['/weight']),
        getter=get_username,
        state=MeasureSG.start_weight
    ),
    Window(
        Format(LEXICON_RU['/measure']),
        getter=get_username,
        state=MeasureSG.start_measure
    )
)

# TODO: add nessesary Windows
setup_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/setup']),
        state=SetupSG.start_setup
    )
)

# TODO: add functionality for parsing account`s details from Telegram
# TODO: add nessesary Windows
account_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/account']),
        # add some getter here for parsing data
        state=AccountSG.start_account
    )
)

# TODO: add nessesary Windows
report_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/report']),
        state=ReportSG.start_report,
        # TODO: ucomment getter`s row
        # getter=get_user_data
    )
)

# TODO: add nessesary Windows
support_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/support']),
        state=SupportSG.start_support,
        # TODO: ucomment getter`s row
        # getter=get_user_data
    )
)

# TODO: add nessesary Windows
contacts_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/contacts']),
        state=ContactsSG.start_contacts
    )
)
