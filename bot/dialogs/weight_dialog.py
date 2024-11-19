from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Row

# TODO: refactor imports
from bot.dialogs.getters import weight_getter
from bot.dialogs.states import AddWeightSG
from bot.dialogs.dialogs_handlers import cancel_btn_clicked
from bot.dialogs.weight_handlers import validate_weight, weight_correct_handler, weight_error_handler, weight_approved, change_weight


add_weight_dialog = Dialog(
    Window(
        Const("Отправьте ваш вес в кг\n" "Можно с точностью до сотых"),
        TextInput(
            id="add_weight",
            type_factory=validate_weight,
            on_success=weight_correct_handler,  # type: ignore
            on_error=weight_error_handler,  # type: ignore
        ),
        Button(
            Const("Отмена"),
            id="cancel_record",
            on_click=cancel_btn_clicked
        ),
        state=AddWeightSG.add_weight,
    ),
    Window(
        Format("Ваш текущий вес: {user_weight}\n"),
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
                on_click=change_weight
            )
        ),
        Button(
            Const("Отмена"),
            id="cancel_record",
            on_click=cancel_btn_clicked
        ),
        state=AddWeightSG.weight_done,
        getter=weight_getter
    ),
)
