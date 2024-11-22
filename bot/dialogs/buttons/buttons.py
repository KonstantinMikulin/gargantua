from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.aiogram_dialog_handlers import cancel_btn_clicked

CANCEL_BUTTON = Button(
    Const("Отмена"),
    id="cancel_record",
    on_click=cancel_btn_clicked
)
