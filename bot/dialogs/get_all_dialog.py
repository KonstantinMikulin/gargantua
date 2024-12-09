from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format, List

from bot.dialogs import GetAllRecordsSG
from bot.dialogs.getters import all_weights_getter

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
            text="Вы еще не вносили показатели <b>веса</b>\n"
            "Используйте команду /weight для записи веса",
            when="no_weights",
        ),
        List(
            Format("{item[0]}: <b>{item[1]}</b>"),
            items="all_weights"
        ),
        CHOOSE_ALL_MEASUREMENTS_BUTTONS,
        OKEY_START_BUTTON,
        state=GetAllRecordsSG.get_all_weights,
        getter=all_weights_getter,  # type:ignore
    )
)
