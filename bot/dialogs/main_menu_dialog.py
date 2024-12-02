from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.states import MainMenuSG
from bot.dialogs.aiogram_dialog_handlers import weight_main_btn


main_menu_dialog = Dialog(
    Window(
        Const("Основное меню"),
        Button(
            Const("Вес"),
            id="one",
            on_click=weight_main_btn
            ),
        Button(Const("Two"), id="two"),
        Button(Const("Three"), id="three"),
        state=MainMenuSG.main_state
    )
)
