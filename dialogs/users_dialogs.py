from aiogram.fsm.state import State, StatesGroup
from aiogram.types import User

from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.text import Const, Format

from lexicon.lexicon import LEXICON_RU


# temporary state group for testing
class UserSG(StatesGroup):
    start_dialog = State()
    help_dialog = State()
    desc_dialog = State()
    

# temporary state group for testing Gargantua`s story  
class WhatSG(StatesGroup):
    start_what = State()
    
    
# temp state group for testing weight saving data
class MeasureSG(StatesGroup):
    start_weight = State()
        
    
async def get_username(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict[str, str]:
    return {'username': event_from_user.username}


user_dialog = Dialog(
    Window(
        Format(LEXICON_RU['/start']),
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

what_dialog = Dialog(
    Window(
        Const(LEXICON_RU['/what']),
        state=WhatSG.start_what
    )
)

measure_dialog = Dialog(
    Window(
        Format(LEXICON_RU['/weight']),
        getter=get_username,
        state=MeasureSG.start_weight
    )
)