from aiogram.types import Message, CallbackQuery, User

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from bot.db import add_weight


def validate_weight(text: str) -> str | None:
    weight = round(float(text), 2)
    if 20 <= weight <= 200:
        return text

    raise ValueError


async def weight_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    weight = round(float(text), 2)
    session = dialog_manager.middleware_data.get("session")
    user: User = dialog_manager.middleware_data.get("event_from_user") # type:ignore
    
    await add_weight(
        session=session,  # type:ignore
        telegram_id=user.id,
        weight=weight,
    )

    await message.answer(f"Ваш текущий вес: {weight} кг был сохранен")
    await dialog_manager.done()


async def weight_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    await message.answer("The weight must be int or float")


# handler for cancel button
async def cancel_btn_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    await callback.message.edit_text("Запись отменена") # type:ignore
    await dialog_manager.done()
