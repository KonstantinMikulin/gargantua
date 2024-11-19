from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.states import AddWeightSG
from bot.dialogs.dialogs_handlers import validate_weight, weight_correct_handler, weight_error_handler, cancel_btn_clicked


add_weight_dialog = Dialog(
    Window(
        Const(
            "Введите ваш вес в кг\n"
            "Можно с точностью до сотых"
            ),
        TextInput(
            id="add_weight",
            type_factory=validate_weight,
            on_success=weight_correct_handler,  # type: ignore
            on_error=weight_error_handler,  # type: ignore
        ),
        Button(
            Const("Отменить"),
            id="cancel_weight",
            on_click=cancel_btn_clicked
        ),
        state=AddWeightSG.add_weight
    )
)
