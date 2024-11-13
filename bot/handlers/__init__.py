from aiogram import Router
from .user_commands import user_router
from .user_weight_command import user_weight_router

__all__ = ["user_router", "user_weight_router"]


# function for assemling all routers
def get_commands_routers() -> list[Router]:
    return [user_router, user_weight_router]
