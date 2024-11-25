from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Row

from bot.dialogs import GetLastRecordsSG
from bot.dialogs.aiogram_dialog_handlers import get_last_measurment
from bot.dialogs.buttons import CANCEL_BUTTON
from bot.dialogs.getters import last_weight_getter, last_chest_getter, last_waist_getter

# TODO: reorganize buttons? Place button "Weight" separately
CHOOSE_BUTTONS = Row(
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
                    ),
                    Button(
                        Const("Вес"), id="get_last_weight", on_click=get_last_measurment
                    )
                )

get_last_records_dialog = Dialog(
    Window(
        Const("Какую запись вы хотите посмотреть?"),
        CHOOSE_BUTTONS,
        CANCEL_BUTTON,
        state=GetLastRecordsSG.choose,
    ),
    Window(
        Const(
            text="Вы еще не вносили замеры <b>груди</b>\n"
            "Используйте команду /measure для записи замеров",
            when="no_chest",
        ),
        Const(
            text="Предыдущая запись <b>замера груди</b>\n", when="last_chest"
        ),
        Format(
            text="Дата: <b>{last_chest_date}</b>\nГрудь: <b>{last_chest}</b> см",
            when="last_chest",
        ),
        CHOOSE_BUTTONS,
        CANCEL_BUTTON,
        state=GetLastRecordsSG.get_chest,
        getter=last_chest_getter,  # type:ignore
    ),
    Window(
        Const(
            text="Вы еще не вносили замеры <b>талии</b>\n"
            "Используйте команду /measure для записи замеров",
            when="no_waist",
        ),
        Const(
            text="Предыдущая запись <b>замера груди</b>\n", when="last_waist"
        ),
        Format(
            text="Дата: <b>{last_waist_date}</b>\nГрудь: <b>{last_waist}</b> см",
            when="last_waist",
        ),
        CHOOSE_BUTTONS,
        CANCEL_BUTTON,
        state=GetLastRecordsSG.get_waist,
        getter=last_waist_getter,  # type:ignore
    ),
    Window(
        Const(
            text="Вы еще не вносили показатели <b>веса</b>\n"
            "Используйте команду /weight для записи веса",
            when="no_weight",
        ),
        Const(text="Предыдущая запись <b>веса</b>\n", when="last_weight"),
        Format(
            text="Дата: <b>{last_weight_date}</b>\nВес: <b>{last_weight}</b> кг",
            when="last_weight",
        ),
        CHOOSE_BUTTONS,
        CANCEL_BUTTON,
        state=GetLastRecordsSG.get_weight,
        getter=last_weight_getter,  # type:ignore
    ),
)
