from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format, List

from bot.dialogs import GetAllRecordsSG
from bot.dialogs.getters import (
    all_weights_getter,
    all_chest_getter,
    all_waist_getter,
    all_hips_getter
)

from bot.dialogs.buttons import (
    CANCEL_START_BUTTON,
    OKEY_START_BUTTON,
    CHOOSE_ALL_MEASUREMENTS_BUTTONS
    )

get_all_records_dialog = Dialog(
    Window(
        Const("Какие записи вы хотите посмотреть?"),
        CHOOSE_ALL_MEASUREMENTS_BUTTONS,
        CANCEL_START_BUTTON,
        state=GetAllRecordsSG.choose,
    ),
    Window(
        Const(
            text="Вы еще не вносили замеры <b>груди</b>\n"
            "Используйте команду /measure для записи замеров",
            when="no_chest",
        ),
        List(Format("{item[0]}: <b>{item[1]}</b> см"), items="all_chest", when="all_chest"),
        CHOOSE_ALL_MEASUREMENTS_BUTTONS,
        OKEY_START_BUTTON,
        state=GetAllRecordsSG.get_all_chest,
        getter=all_chest_getter,  # type:ignore
    ),
    Window(
        Const(
            text="Вы еще не вносили замеры <b>талии</b>\n"
            "Используйте команду /measure для записи замеров",
            when="no_waist",
        ),
        List(Format("{item[0]}: <b>{item[1]}</b> см"), items="all_waist", when="all_waist"),
        CHOOSE_ALL_MEASUREMENTS_BUTTONS,
        OKEY_START_BUTTON,
        state=GetAllRecordsSG.get_all_waist,
        getter=all_waist_getter,  # type:ignore
    ),
    Window(
        Const(
            text="Вы еще не вносили замеры <b>бёдер</b>\n"
            "Используйте команду /measure для записи замеров",
            when="no_hips",
        ),
        List(Format("{item[0]}: <b>{item[1]}</b> см"), items="all_hips", when="all_hips"),
        CHOOSE_ALL_MEASUREMENTS_BUTTONS,
        OKEY_START_BUTTON,
        state=GetAllRecordsSG.get_all_hips,
        getter=all_hips_getter,  # type:ignore
    ),
    Window(
        Const(
            text="Вы еще не вносили показатели <b>веса</b>\n"
            "Используйте команду /weight для записи веса",
            when="no_weights",
        ),
        List(Format("{item[0]}: <b>{item[1]}</b> кг"), items="all_weights", when="all_weights"),
        CHOOSE_ALL_MEASUREMENTS_BUTTONS,
        OKEY_START_BUTTON,
        state=GetAllRecordsSG.get_all_weights,
        getter=all_weights_getter,  # type:ignore
    ),
)
