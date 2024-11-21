from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Row

get_last_records_dialog = Dialog(
    Window(
        Const("Какую запись вы хотите посмотреть?"),
        Row(
            Button(
                Const("Грудь"),
                id="get_last_chest",
                on_click=
            )
        )
    )
)
