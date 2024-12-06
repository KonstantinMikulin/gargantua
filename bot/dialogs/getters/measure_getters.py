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


# TODO: count delta if time between records is one week or more
async def measurements_delta_getter(
    dialog_manager: DialogManager, event_from_user: User, **kwargs
) -> dict[str, float | str]:
    current_chest = dialog_manager.dialog_data.get("chest")
    current_waist = dialog_manager.dialog_data.get("waist")
    current_hips = dialog_manager.dialog_data.get("hips")
    
    prev_chest = dialog_manager.dialog_data.get("prev_chest")
    prev_waist = dialog_manager.dialog_data.get("prev_waist")
    prev_hips = dialog_manager.dialog_data.get("prev_hips")
    
    getter_dict = {
        "is_delta": False,
        "is_chest_delta": False,
        "chest": current_chest,
        "is_waist_delta": False,
        "waist": current_waist,
        "is_hips_delta": False,
        "hips": current_hips
    }
    
    if all([prev_chest, prev_waist, prev_hips]):
        chest_delta = abs(prev_chest - current_chest)  # type: ignore
        waist_delta = abs(prev_waist - current_waist)  # type: ignore
        hips_delta = abs(prev_hips - current_hips)  # type: ignore
        deltas = [chest_delta, waist_delta, hips_delta]
        
        for delta in deltas:
            if delta >= 1 and delta is chest_delta:
                getter_dict.update(
                    {
                        "is_delta": True,
                        "is_chest_delta": True,
                        "chest_chest": current_chest,  # type: ignore
                        "chest_gain_loose": "меньше" if current_chest < prev_chest else "больше", # type:ignore
                        "chest_delta": round(chest_delta, 2),
                    }
                )
            elif delta >= 1 and delta is waist_delta:
                getter_dict.update(
                    {
                        "is_delta": True,
                        "is_waist_delta": True,
                        "waist": current_waist,  # type: ignore
                        "waist_gain_loose": "меньше" if current_waist < prev_waist else "больше",  # type: ignore
                        "waist_delta": round(waist_delta, 2),
                    }
                )
            elif delta >= 1 and delta is hips_delta:
                getter_dict.update(
                    {
                        "is_delta": True,
                        "is_hips_delta": True,
                        "hips": current_hips,  # type: ignore
                        "hips_gain_loose": "меньше" if current_hips < prev_hips else "больше", # type: ignore
                        "hips_delta": round(hips_delta, 2),
                    }
                )
        
    return getter_dict  # type: ignore
