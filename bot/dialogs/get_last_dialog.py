from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs import GetLastRecordsSG
from bot.dialogs.getters import last_weight_getter, last_chest_getter, last_waist_getter, last_hips_getter
from bot.dialogs.buttons import CANCEL_START_BUTTON, CHOOSE_MEASUREMENTS_BUTTONS

get_last_records_dialog = Dialog(
    Window(
        Const("Какую запись вы хотите посмотреть?"),
        CHOOSE_MEASUREMENTS_BUTTONS,
        CANCEL_START_BUTTON,
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
        CHOOSE_MEASUREMENTS_BUTTONS,
        CANCEL_START_BUTTON,
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
            text="Предыдущая запись <b>замера талии</b>\n", when="last_waist"
        ),
        Format(
            text="Дата: <b>{last_waist_date}</b>\nТалия: <b>{last_waist}</b> см",
            when="last_waist",
        ),
        CHOOSE_MEASUREMENTS_BUTTONS,
        CANCEL_START_BUTTON,
        state=GetLastRecordsSG.get_waist,
        getter=last_waist_getter,  # type:ignore
    ),
    Window(
        Const(
            text="Вы еще не вносили замеры <b>бёдер</b>\n"
            "Используйте команду /measure для записи замеров",
            when="no_hips",
        ),
        Const(text="Предыдущая запись <b>замера бёдер</b>\n", when="last_hips"),
        Format(
            text="Дата: <b>{last_hips_date}</b>\nБёдра: <b>{last_hips}</b> см",
            when="last_hips",
        ),
        CHOOSE_MEASUREMENTS_BUTTONS,
        CANCEL_START_BUTTON,
        state=GetLastRecordsSG.get_hips,
        getter=last_hips_getter,  # type:ignore
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
        CHOOSE_MEASUREMENTS_BUTTONS,
        CANCEL_START_BUTTON,
        state=GetLastRecordsSG.get_weight,
        getter=last_weight_getter,  # type:ignore
    ),
)
