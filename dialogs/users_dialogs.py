from aiogram.types import User

from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Row

from lexicon.lexicon import LEXICON_RU
from handlers.aiogram_dialog_handlers import account_yes_get_clicked, account_no_get_clicked
from states.aiogram_dialog_states import (
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
from getters.aiogram_dialog_getters import get_username


# TODO: add nessesary Windows
start_dialog = Dialog(
    Window(
        Format(LEXICON_RU['/start']['step_1']),
        getter=get_username,
        state=StartSG.start_dialog
    ),
    Window(
        Const(LEXICON_RU['/start']['step_2']),
        state=StartSG.start_dialog_help
    ),
    Window(
        Const(LEXICON_RU['/start']['step_3']),
        state=StartSG.start_dialog_desc
    ),
    Window(
        Const(LEXICON_RU['/start']['step_4']),
        Row(
            Button(text=Const('Yes'), id='yes', on_click=account_yes_get_clicked),
            Button(Const('No'), id='no', on_click=account_no_get_clicked)
        ),
        state=StartSG.create_account_on_start
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
    ),
    # Window(
    #     TextInput(
    #         id='support_msg',
    #         type_factory=str,
    #         on_success=
    #     )
    # )
)

# TODO: add nessesary Windows
contacts_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/contacts']),
        state=ContactsSG.start_contacts
    )
)
