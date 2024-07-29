from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format, List
from aiogram_dialog.widgets.kbd import Button, Row, Url
from getters.aiogram_dialog_getters import get_username, get_commands

from lexicon.lexicon import LEXICON_RU
from handlers.ad_handlers import (
    profile_create_click,
)
from states.users_dialog_states import (
    DefaultSG,
    StartSG,
    HelpSG,
    DescSG,
    WhatSG,
    MeasureSG,
    SetupSG,
    profileSG,
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
        Button(text=Const('Weight'), id='weight_menu', on_click=None),
        Button(text=Const('Measure'), id='measure_menu', on_click=None),
        state=DefaultSG.default_dialog
    )
)

start_dialog = Dialog(
    Window(
        Format(LEXICON_RU['/start']),
        Row(
            Button(text=Const('Yes'), id='profile_yes', on_click=profile_create_click),
            Button(Const('No'), id='profile_no', on_click=profile_create_click),
            
        ),
        getter=get_username,
        state=StartSG.start_dialog
    )
)

# /help dialog
help_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/help']),
        List(
            field=Format('{item[0]} - {item[1]}'),
            items='commands'
        ),
        getter=get_commands,
        state=HelpSG.start_help,
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

# TODO: add functionality for parsing profile`s details from Telegram
# TODO: add nessesary Windows
profile_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/profile']),
        # add some getter here for parsing data
        state=profileSG.start_profile
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
