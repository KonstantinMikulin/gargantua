from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.states import MainMenuSG


main_menu_dialog = Dialog(
    Window(
        Const("Основное меню"),
        Button(Const("One"), id="one"),
        Button(Const("Two"), id="two"),
        Button(Const("Three"), id="three"),
        state=MainMenuSG.main_state
    )
)