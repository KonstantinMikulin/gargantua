from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Row

from bot.dialogs.states import AddMeasurmentsSG
from bot.dialogs.aiogram_dialog_handlers import cancel_btn_clicked
from bot.dialogs.aiogram_dialog_handlers import (
    validate_measurement,
    chest_correct_handler,
    chest_error_handler,
    waist_correct_handler,
    waist_error_handler,
    hips_correct_handler,
    hips_error_handler,
    change_measurments,
    measurements_approved,
    okey_clicked
)
from bot.dialogs.getters import measurments_getter, measurements_delta_getter

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
        Const(text="Всё верно?"),
        Row(
            Button(
                Const("Да"),
                id="appove_measure",
                on_click=measurements_approved,  # type: ignore
            ),
            Button(
                Const("Изменить..."),
                id="change_measure",
                on_click=change_measurments,
            ),
        ),
        Button(
            Const("Отмена"), id="cancel_record", on_click=cancel_btn_clicked
        ),
        state=AddMeasurmentsSG.check_measure,
        getter=measurments_getter,
    ),
    Window(
        Const("Какие замеры изменить?"),
        Button(Const("Грудь"), id="change_chest", on_click=change_measurments),
        Button(Const("Талия"), id="change_waist", on_click=change_measurments),
        Button(Const("Бёдра"), id="change_hips", on_click=change_measurments),
        state=AddMeasurmentsSG.change_measure,
    ),
    Window(
        Format(
            text="Итак. У нас изменилось:\n",
            when="is_delta"
        ),
        Format(
            text="Грудь {chest_gain_loose} на <b>{chest_delta} см</b>",
            when="is_chest_delta",
        ),
        Format(
            text="Талия {waist_gain_loose} на <b>{waist_delta} см</b>",
            when="is_waist_delta",
        ),
        Format(
            text="Бёдра {hips_gain_loose} на <b>{hips_delta} см</b>",
            when="is_hips_delta",
        ),
        Button(
            text=Const("Ok"),
            id="okey",
            on_click=okey_clicked
        ),
        state=AddMeasurmentsSG.measurements_progress,
        getter=measurements_delta_getter
    ),
)

