from aiogram import Router
#TODO: change all imports to absolute
from .user_commands import user_router
from .user_weight_command import user_weight_router
from .user_measurments_cmds import user_measure_router
from bot.handlers.user_cb_handlers import user_callback_router

__all__ = [
    "user_router",
    "user_weight_router",
    "user_measure_router",
    "user_callback_router",
]


# function for assemling all routers
def get_commands_routers() -> list[Router]:
    return [
    user_router,
    user_weight_router,
    user_measure_router,
    user_callback_router
    ]
