from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.states import AddMeasurmentsSG
from bot.dialogs.dialogs_handlers import cancel_btn_clicked
from bot.dialogs.measurements_handlers import (
    validate_measurement,
    chest_correct_handler,
    chest_error_handler,
    waist_correct_handler,
    waist_error_handler,
    hips_correct_handler,
    hips_error_handler
)

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
            Const("Отмена"),
            id="cancel_record",
            on_click=cancel_btn_clicked
        ),
        state=AddMeasurmentsSG.add_hips,
    ),
)
