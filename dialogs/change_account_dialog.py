from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button, Row, Column
from aiogram_dialog.widgets.media import DynamicMedia

from handlers.ad_fill_account_handlers import (
    name_correct_nandler,
    name_error_nandler
)

from states.users_dialog_states import ChangeAccountSG

# dialog for changing account
change_account_dialog = Dialog(
    Window(
        Const('Enter your name, please'),
        TextInput(
            id='change_name',
            on_success=name_correct_nandler,
            on_error=name_error_nandler # type: ignore
        ),
        state=ChangeAccountSG.change_name
    )
)