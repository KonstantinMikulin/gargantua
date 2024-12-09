from datetime import datetime
from typing import Any

from aiogram.types import User

from aiogram_dialog import DialogManager


from bot.db import get_last_weight, get_all_weights


async def weight_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs
) -> dict[str, float]:
    return {"user_weight": dialog_manager.dialog_data.get("weight")} # type:ignore


async def all_weights_getter(
    dialog_manager: DialogManager, event_from_user: User, **kwargs
) -> dict[str, tuple[tuple[Any]] | bool]:
    session = dialog_manager.middleware_data.get("session")
    weights = await get_all_weights(
        session=session,  # type:ignore
        telegram_id=event_from_user.id,
    )

    print(f"This is list of weights: {weights}")
    
    if weights:
        weights_list = []
        for weight in weights:
            try:
                date = datetime.fromisoformat(str(weight.created_at))  # type:ignore
                formatted_date = date.strftime("%d.%m.%Y")
            except ValueError:
                formatted_date = None
                
            weights_list.append((formatted_date, weight.weight))
            
        return {"all_weights": tuple(weights_list)} # type: ignore
    else:
        return {"no_weights": True}


async def last_weight_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs
) -> dict[str, float | str]:
    session = dialog_manager.middleware_data.get("session")
    weight = await get_last_weight(
        session=session,  # type:ignore
        telegram_id=event_from_user.id,
    ) 
    
    if weight:
        try:
            date = datetime.fromisoformat(str(weight.created_at))  # type:ignore
            formatted_date = date.strftime("%d.%m.%Y")
        except ValueError:
            formatted_date = None

        return {
            "last_weight_date": formatted_date,  # type:ignore
            "last_weight": weight.weight,  # type:ignore
        }
    else:
        return {"no_weight": True}


# TODO: count delta if time between records is one week or more
async def weight_delta_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs
) -> dict[str, float | str]:
    current_weight = dialog_manager.dialog_data.get("weight")
    prev_weight = dialog_manager.dialog_data.get("prev_weight")
    
    if prev_weight is not None:    
        weight_delta = abs(prev_weight - current_weight)  # type: ignore
        
        if weight_delta >= 1:
            return {
                "is_delta": True,
                "weight": current_weight,  # type: ignore
                "gain_loose": "сбросили"
                if current_weight < prev_weight  # type: ignore
                else "набрали",
                "weight_delta": round(weight_delta, 2)
            }
    
    return {"is_delta": False, "weight": current_weight} # type: ignore