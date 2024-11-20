from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Row

from bot.dialogs.states import AddMeasurmentsSG
from bot.dialogs.dialogs_handlers import cancel_btn_clicked
from bot.dialogs.measure_handlers import (
    validate_measurement,
    chest_correct_handler,
    chest_error_handler,
    waist_correct_handler,
    waist_error_handler,
    hips_correct_handler,
    hips_error_handler,
    measurements_approved
)
from bot.dialogs.getters import measurments_getter

add_measurments_dialog = Dialog(
    Window(
        Const("Отправьте обхват груди в см\n"),
        TextInput(
            id="add_chest",
            type_factory=validate_measurement,
            on_success=chest_correct_handler,
            on_error=chest_error_handler,  # type:ignore
        ),
        Button(
            Const("Отмена"), id="cancel_record", on_click=cancel_btn_clicked
        ),
        state=AddMeasurmentsSG.add_chest,
    ),
    Window(
        Const("Отправьте обхват талии в см\n"),
        TextInput(
            id="add_waist",
            type_factory=validate_measurement,
            on_success=waist_correct_handler,
            on_error=waist_error_handler,  # type:ignore
        ),
        Button(
            Const("Отмена"), id="cancel_record", on_click=cancel_btn_clicked
        ),
        state=AddMeasurmentsSG.add_waist,
    ),
    Window(
        Const("Отправьте обхват бёдер в см\n"),
        TextInput(
            id="add_hips",
            type_factory=validate_measurement,
            on_success=hips_correct_handler,
            on_error=hips_error_handler,  # type:ignore
        ),
        Button(
            Const("Отмена"), id="cancel_record", on_click=cancel_btn_clicked
        ),
        state=AddMeasurmentsSG.add_hips,
    ),
    Window(
        Format(
            "Ваши замеры\n"
            "Объём груди: <b>{user_chest}</b> см\n"
            "Объём талии: <b>{user_waist}</b> см\n"
            "Объём бёдер: <b>{user_hips}</b> см\n"
        ),
        Const("Всё верно?"),
        Row(
            Button(
                Const("Да"),
                id="measure_appove",
                on_click=measurements_approved,  # type: ignore
            ),
            Button(
                Const("Изменить..."),
                id="change_measure",
                # TODO: change this function
                on_click=measurements_approved,
            ),
        ),
        Button(
            Const("Отмена"), id="cancel_record", on_click=cancel_btn_clicked
        ),
        state=AddMeasurmentsSG.measure_check,
        getter=measurments_getter
    ),
)
