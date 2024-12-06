from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs import GetAllRecordsSG

from bot.dialogs.buttons import (
    CANCEL_START_BUTTON,
    CHOOSE_ALL_MEASUREMENTS_BUTTONS
    )

get_all_records_dialog = Dialog(
    Window(
        Const("Какие записи вы хотите посмотреть?"),
        CHOOSE_ALL_MEASUREMENTS_BUTTONS,
        CANCEL_START_BUTTON,
        state=GetAllRecordsSG.choose
    ),
    Window
)
