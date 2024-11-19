from aiogram.types import Message, User

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

from sqlalchemy.ext.asyncio import AsyncSession

from bot.dialogs.states import AddMeasurmentsSG
from bot.db import add_chest, add_waist, add_hips


def validate_measurement(text: str) -> str | None:
    measurment = round(float(text), 2)
    if 20 <= measurment <= 200:
        return text
    
    raise ValueError


async def chest_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    measurment = round(float(text), 2)
    dialog_manager.dialog_data["chest"] = measurment

    await dialog_manager.switch_to(state=AddMeasurmentsSG.add_waist)
    await message.answer(f"Ваш обхват груди {measurment} см был сохранен")


async def chest_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    await message.answer(
        "Обхват груди должен быть числом"
    )


async def waist_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    measurment = round(float(text), 2)
    dialog_manager.dialog_data["waist"] = measurment

    await dialog_manager.switch_to(state=AddMeasurmentsSG.add_hips)
    await message.answer(f"Обхват талии {measurment} см был сохранен")


async def waist_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    await message.answer("Обхват талии должен быть числом")
    
    
async def hips_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    measurment = round(float(text), 2)
    
    chest = dialog_manager.dialog_data.get("chest")
    waist = dialog_manager.dialog_data.get("waist")
    hips = measurment

    session: AsyncSession = dialog_manager.middleware_data.get("session")  # type:ignore
    user: User = dialog_manager.middleware_data.get("event_from_user")  # type:ignore

    await add_chest(
        session=session,
        telegram_id=user.id,
        chest=chest  # type:ignore
    )
    
    await add_waist(
        session=session,
        telegram_id=user.id,
        waist=waist  # type:ignore
    )
    
    await add_hips(
        session=session,
        telegram_id=user.id,
        hips=hips
    )
    
    await dialog_manager.done()
    
    await message.answer(f"Обхват бёдер {measurment} см был сохранен")


async def hips_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    await message.answer("Обхват бёдер должен быть числом")
