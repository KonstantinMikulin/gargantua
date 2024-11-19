from aiogram.types import User

from aiogram_dialog import DialogManager


async def weight_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs
) -> dict[str, float]:
    return {"user_weight": dialog_manager.dialog_data.get("weight")} # type:ignore
