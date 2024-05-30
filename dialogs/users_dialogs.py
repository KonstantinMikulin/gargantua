from aiogram.fsm.state import State, StatesGroup
from aiogram.types import User

from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.text import Const, Format, Multi

from lexicon.lexicon import LEXICON_RU


# draft state group for testing
# TODO: add nessesary States
class UserSG(StatesGroup):
    start_dialog = State()
    help_dialog = State()
    desc_dialog = State()
    

# draft state group for testing Gargantua`s story  
# TODO: add nessesary States
class WhatSG(StatesGroup):
    start_what = State()
    
    
# draft state group for testing weight saving data
# TODO: add nessesary States
class MeasureSG(StatesGroup):
    start_weight = State()
    start_measure = State()
        

# draft state group for testing bot`s setup
# TODO: add nessesary States
class SetupSG(StatesGroup):
    start_setup = State()
    
    
# draft state group for testing user`s account details
# TODO: add nessesary States
class AccountSG(StatesGroup):
    start_account = State()
    

# getter for username
async def get_username(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict[str, str]:
    return {'username': event_from_user.username}


# TODO: add nessesary Windows
user_start_dialog = Dialog(
    # TODO: change this Window for sending parts of text with delay
    Window(
        Multi(
            Format(LEXICON_RU['/start']['step_1']),
            Const(LEXICON_RU['/start']['step_2']),
            Const(LEXICON_RU['/start']['step_3']),
            sep='\n\n'
        ),
        getter=get_username,
        state=UserSG.start_dialog
    ),
    Window(
        Const(LEXICON_RU['/help']),
        state=UserSG.help_dialog
    ),
    Window(
        Const(LEXICON_RU['/desc']),
        state=UserSG.desc_dialog
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