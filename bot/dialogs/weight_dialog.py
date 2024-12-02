from aiogram_dialog import Dialog, Window, StartMode, ShowMode
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Row, Start

# TODO: refactor imports
from bot.dialogs.getters import weight_getter, weight_delta_getter
from bot.dialogs import AddWeightSG
from bot.dialogs.states import MainMenuSG
from bot.dialogs.aiogram_dialog_handlers import (
    validate_weight,
    weight_correct_handler,
    weight_error_handler,
    weight_approved,
    change_weight
)

# buttton to switch to main_menu state (call it "cancel")
_CANCEL_BUTTON = Start(
    text=Const("Отмена"),
    id="cancel_switch_to_main",
    state=MainMenuSG.main_state,
    show_mode=ShowMode.DELETE_AND_SEND,
    mode=StartMode.RESET_STACK,
)

add_weight_dialog = Dialog(
    Window(
        Const("Отправьте ваш вес в кг\n" "Можно с точностью до сотых"),
        TextInput(
            id="add_weight",
            type_factory=validate_weight,
            on_success=weight_correct_handler,  # type: ignore
            on_error=weight_error_handler,  # type: ignore
        ),
        _CANCEL_BUTTON,
        state=AddWeightSG.add_weight,
    ),
    Window(
        Format("Ваш текущий вес: <b>{user_weight}</b> кг"),
        Const("Сохраняем?"),
        Row(
            Button(
                Const("Да"),
                id="weight_appove",
                on_click=weight_approved,  # type: ignore
            ),
            Button(
                Const("Изменить вес"),
                id="change_weight",
                on_click=change_weight,
            ),
        ),
        _CANCEL_BUTTON,
        state=AddWeightSG.weight_done,
        getter=weight_getter,
    ),
    Window(
        Format("Ваш текущий вес <b>{weight}</b> кг был сохранен\n"),
        Format(
            text="С прошлого взвешивания вы {gain_loose}\n<b>{weight_delta}</b> кг",
            when="is_delta",
        ),
        _CANCEL_BUTTON,
        state=AddWeightSG.weight_progress,
        getter=weight_delta_getter
    ),
)
