import datetime

from aiogram.types import User

from aiogram_dialog import DialogManager


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



