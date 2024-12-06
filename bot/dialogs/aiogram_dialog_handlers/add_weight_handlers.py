from aiogram.types import Message, CallbackQuery, User

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from bot.db import add_weight, get_last_weight

from bot.dialogs import AddWeightSG


def validate_weight(text: str) -> str | None:
    weight = round(float(text), 2)
    if 20 <= weight <= 200:
        return text

    raise ValueError


async def weight_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    session = dialog_manager.middleware_data.get("session")
    weight = round(float(text), 2)
    dialog_manager.dialog_data["weight"] = weight
    prev_weight = await get_last_weight(
            session=session,  # type:ignore
            telegram_id=message.from_user.id, # type: ignore
        )
    
    if prev_weight is not None:
        dialog_manager.dialog_data["prev_weight"] = prev_weight.weight  # type: ignore

    await dialog_manager.switch_to(state=AddWeightSG.check_weight)
    
    
async def weight_approved(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    weight = dialog_manager.dialog_data.get("weight")
    session = dialog_manager.middleware_data.get("session")
    user: User = dialog_manager.middleware_data.get("event_from_user")  # type:ignore

    await dialog_manager.switch_to(state=AddWeightSG.weight_progress, show_mode=ShowMode.AUTO)
    
    await add_weight(
        session=session,  # type:ignore
        telegram_id=user.id,
        weight=weight,  # type:ignore
    )


async def change_weight(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    await dialog_manager.switch_to(state=AddWeightSG.add_weight, show_mode=ShowMode.DELETE_AND_SEND)


async def weight_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    await message.answer("Вес должен быть числом\n")
    