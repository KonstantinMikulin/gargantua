from aiogram.types import Message, User, CallbackQuery

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs import AddMeasurmentsSG
from bot.db import add_chest, add_waist, add_hips, get_last_chest, get_last_waist, get_last_hips


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
    session = dialog_manager.middleware_data.get("session")
    prev_chest = await get_last_chest(
        session=session,  # type: ignore
        telegram_id=message.from_user.id,  # type: ignore
    )
    
    if prev_chest is not None:
        dialog_manager.dialog_data["prev_chest"] = prev_chest.measurement  # type: ignore

    measurment = round(float(text), 2)
    
    if dialog_manager.dialog_data.get("chest") is None:
        dialog_manager.dialog_data["chest"] = measurment
        await dialog_manager.switch_to(state=AddMeasurmentsSG.add_waist)
    else:
        dialog_manager.dialog_data["chest"] = measurment
        await dialog_manager.switch_to(state=AddMeasurmentsSG.check_measure)


async def chest_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    await message.answer("Обхват груди должен быть числом")


async def waist_correct_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    session = dialog_manager.middleware_data.get("session")
    prev_waist = await get_last_waist(
        session=session,  # type: ignore
        telegram_id=message.from_user.id,  # type: ignore
    )
    if prev_waist is not None:
        dialog_manager.dialog_data["prev_waist"] = prev_waist.measurement  # type: ignore

    measurment = round(float(text), 2)

    if dialog_manager.dialog_data.get("waist") is None:
        dialog_manager.dialog_data["waist"] = measurment
        await dialog_manager.switch_to(state=AddMeasurmentsSG.add_hips)
    else:
        dialog_manager.dialog_data["waist"] = measurment
        await dialog_manager.switch_to(state=AddMeasurmentsSG.check_measure)


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
    session = dialog_manager.middleware_data.get("session")
    prev_hips = await get_last_hips(
        session=session,  # type: ignore
        telegram_id=message.from_user.id,  # type: ignore
    )
    if prev_hips is not None:
        dialog_manager.dialog_data["prev_hips"] = prev_hips.measurement  # type: ignore

    measurment = round(float(text), 2)

    if dialog_manager.dialog_data.get("hips") is None:
        dialog_manager.dialog_data["hips"] = measurment
        await dialog_manager.switch_to(state=AddMeasurmentsSG.check_measure)
    else:
        dialog_manager.dialog_data["hips"] = measurment
        await dialog_manager.switch_to(state=AddMeasurmentsSG.check_measure)
    
    
async def hips_error_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    await message.answer("Обхват бёдер должен быть числом")


async def change_measurments(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    if button.widget_id == "change_measure":
        await dialog_manager.switch_to(state=AddMeasurmentsSG.change_measure)
    elif button.widget_id == "change_chest":
        await dialog_manager.switch_to(state=AddMeasurmentsSG.add_chest)
    elif button.widget_id == "change_waist":
        await dialog_manager.switch_to(state=AddMeasurmentsSG.add_waist)
    elif button.widget_id == "change_hips":
        await dialog_manager.switch_to(state=AddMeasurmentsSG.add_hips)
    

    
async def measurements_approved(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
):
    chest = dialog_manager.dialog_data.get("chest")
    waist = dialog_manager.dialog_data.get("waist")
    hips = dialog_manager.dialog_data.get("hips")

    session = dialog_manager.middleware_data.get("session")
    user: User = dialog_manager.middleware_data.get("event_from_user") # type:ignore

    # TODO: refactor these three functions
    await add_chest(
        session=session,  # type:ignore
        telegram_id=user.id,
        chest=chest,  # type:ignore
    )

    await add_waist(
        session=session,  # type:ignore
        telegram_id=user.id,
        waist=waist,  # type:ignore
    )

    await add_hips(
        session=session,  # type:ignore
        telegram_id=user.id,
        hips=hips,  # type:ignore
    )
    
    await dialog_manager.switch_to(state=AddMeasurmentsSG.measurements_progress, show_mode=ShowMode.DELETE_AND_SEND)
