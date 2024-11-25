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
    session = dialog_manager.middleware_data.get("session")

    try:
        weight = await get_last_weight(session=session, telegram_id=event_from_user.id)  # type:ignore
    except AttributeError:
        return {"no_weight": True}
    else:
        try:
            date = datetime.fromisoformat(str(weight.created_at))  # type:ignore
            formatted_date = date.strftime("%d.%m.%Y")
        except ValueError:  # Handle cases where created_at is not ISO formatted
            formatted_date = None

        return {
            "last_weight_date": formatted_date,  # type:ignore
            "last_weight": weight.weight,  # type:ignore
        }
