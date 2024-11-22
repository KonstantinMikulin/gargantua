from datetime import datetime

from aiogram.types import User

from aiogram_dialog import DialogManager

from bot.db import get_last_weight


async def weight_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs
) -> dict[str, float]:
    return {"user_weight": dialog_manager.dialog_data.get("weight")} # type:ignore


async def last_weight_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs
) -> dict[str, float | str]:
    # session = dialog_manager.middleware_data.get("session")
    # weight = await get_last_weight(
    #         session=session,  # type:ignore
    #         telegram_id=event_from_user.id,  # type:ignore
    #     )
    # date = datetime.fromisoformat(str(weight.created_at))  # type:ignore
    # formatted_date = date.strftime("%d.%m.%Y")
    # return {
    #     "last_weight_date": formatted_date,
    #     "last_weight": weight.weight,  # type:ignore
    # }
    
    session = dialog_manager.middleware_data.get("session")

    try:
        weight = await get_last_weight(
            session=session,  # type:ignore
            telegram_id=event_from_user.from_user.id,  # type:ignore
        )
        date = datetime.fromisoformat(str(weight.created_at))  # type:ignore
        formatted_date = date.strftime("%d.%m.%Y")
    except AttributeError:
        return {"no_weight": True}
    else:
        return {
            "last_weight_date": formatted_date,
            "last_weight": weight.weight,  # type:ignore
        }
