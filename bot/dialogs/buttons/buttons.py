from aiogram_dialog import StartMode, ShowMode
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Start

from bot.dialogs import MainMenuSG

# buttton to switch to main_menu state (call it "cancel")
CANCEL_START_BUTTON = Start(
    text=Const("Отмена"),
    id="cancel_switch_to_main",
    state=MainMenuSG.main_state,
    show_mode=ShowMode.DELETE_AND_SEND,
    mode=StartMode.RESET_STACK,
)

# buttton to switch to main_menu state (call it "Ok")
OKEY_START_BUTTON = Start(
    text=Const("Ок"),
    id="okey_switch_to_main",
    state=MainMenuSG.main_state,
    show_mode=ShowMode.DELETE_AND_SEND,
    mode=StartMode.RESET_STACK,
)
