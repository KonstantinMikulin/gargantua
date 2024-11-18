from aiogram.types import Message, User

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

from bot.db import add_weight


def validate_weight(text: str) -> str | None:
    weight = round(float(text), 2)
    if 20 <= weight <= 500:
        return text

    raise ValueError


async def weight_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    weight = round(float(text), 2)
    # dialog_manager.dialog_data["weight"] = weight
    session = dialog_manager.middleware_data.get("session")
    user: User = dialog_manager.middleware_data.get("event_from_user") # type:ignore

    await add_weight(
        session=session,  # type:ignore
        telegram_id=user.id,
        weight=weight,
    )

    await message.answer(
        "You will achieve your goals!"
    )


async def weight_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    await message.answer("The weight must be int or float")
