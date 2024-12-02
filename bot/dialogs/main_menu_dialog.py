from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.states import MainMenuSG
from bot.dialogs.aiogram_dialog_handlers import (
    weight_main_btn,
    measure_main_btn,
    last_main_btn
)


main_menu_dialog = Dialog(
    Window(
        Const("Основное меню"),
        Button(Const("Вес"), id="weight_main_menu", on_click=weight_main_btn),
        Button(
            Const("Записать объемы"),
            id="measure_main_menu",
            on_click=measure_main_btn,
        ),
        Button(
            Const("Предыдущие замеры"),
            id="last_main_menu",
            on_click=last_main_btn
            ),
        state=MainMenuSG.main_state,
    )
)
