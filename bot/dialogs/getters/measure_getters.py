from datetime import datetime

from aiogram.types import User

from aiogram_dialog import DialogManager

from bot.db import get_last_chest, get_last_waist, get_last_hips


async def measurments_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs
) -> dict[str, float]:
    user_chest = dialog_manager.dialog_data.get("chest")
    user_waist = dialog_manager.dialog_data.get("waist")
    user_hips = dialog_manager.dialog_data.get("hips")
    
    return {
        "user_chest": user_chest,  # type:ignore
        "user_waist": user_waist,  # type:ignore
        "user_hips": user_hips  # type:ignore
    }


async def last_chest_getter(
    dialog_manager: DialogManager, event_from_user: User, **kwargs
) -> dict[str, float | str]:
    session = dialog_manager.middleware_data.get("session")
    chest = await get_last_chest(
        session=session,  # type:ignore
        telegram_id=event_from_user.id,
    )

    if chest:
        try:
            date = datetime.fromisoformat(str(chest.created_at))  # type:ignore
            formatted_date = date.strftime("%d.%m.%Y")
        except ValueError:
            formatted_date = None

        return {
            "last_chest_date": formatted_date,  # type:ignore
            "last_chest": chest.measurement,  # type:ignore
        }
    else:
        return {"no_chest": True}


async def last_waist_getter(
    dialog_manager: DialogManager, event_from_user: User, **kwargs
) -> dict[str, float | str]:
    session = dialog_manager.middleware_data.get("session")
    waist = await get_last_waist(
        session=session,  # type:ignore
        telegram_id=event_from_user.id,
    )

    if waist:
        try:
            date = datetime.fromisoformat(str(waist.created_at))  # type:ignore
            formatted_date = date.strftime("%d.%m.%Y")
        except ValueError:
            formatted_date = None

        return {
            "last_waist_date": formatted_date,  # type:ignore
            "last_waist": waist.measurement,  # type:ignore
        }
    else:
        return {"no_waist": True}


async def last_hips_getter(
    dialog_manager: DialogManager, event_from_user: User, **kwargs
) -> dict[str, float | str]:
    session = dialog_manager.middleware_data.get("session")
    hips = await get_last_hips(
        session=session,  # type:ignore
        telegram_id=event_from_user.id,
    )

    if hips:
        try:
            date = datetime.fromisoformat(str(hips.created_at))  # type:ignore
            formatted_date = date.strftime("%d.%m.%Y")
        except ValueError:
            formatted_date = None

        return {
            "last_hips_date": formatted_date,  # type:ignore
            "last_hips": hips.measurement,  # type:ignore
        }
    else:
        return {"no_hips": True}