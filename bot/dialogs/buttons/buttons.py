from aiogram_dialog import StartMode, ShowMode
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, Row, Group, Start

from bot.dialogs import MainMenuSG
from bot.dialogs.aiogram_dialog_handlers import get_last_measurment

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

CHOOSE_LAST_MEASUREMENT_BUTTONS = Group(
    Row(
        Button(
            Const("Грудь"),
            id="get_last_chest",
            on_click=get_last_measurment,
        ),
        Button(
            Const("Талия"),
            id="get_last_waist",
            on_click=get_last_measurment,
        ),
        Button(
            Const("Бёдра"),
            id="get_last_hips",
            on_click=get_last_measurment,
        )
    ),
    Row(
        Button(
            Const("Вес"),
            id="get_last_weight",
            on_click=get_last_measurment
        )
    )
)

CHOOSE_ALL_MEASUREMENTS_BUTTONS = Group(
    Row(
        Button(
            Const("Грудь"),
            id="get_all_chest",
            on_click=get_last_measurment,
        ),
        Button(
            Const("Талия"),
            id="get_all_waist",
            on_click=get_last_measurment,
        ),
        Button(
            Const("Бёдра"),
            id="get_all_hips",
            on_click=get_last_measurment,
        )
    ),
    Row(
        Button(
            Const("Вес"),
            id="get_all_weight",
            on_click=get_last_measurment
        )
    ),
)