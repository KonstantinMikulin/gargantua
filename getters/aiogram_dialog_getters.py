import html
from pprint import pprint

from aiogram.types import User

from aiogram_dialog import DialogManager


# getter for username
async def get_username(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict[str, str | None]:
    return {'username': html.escape(event_from_user.first_name)}


# getter for retrieving data from db
# TODO: make this getter work
# async def get_user_data(dialog_manager: DialogManager, user_data: User, **kwargs) -> dict[str, str | None]:
#     pass


# getter for collecting all commands in one dict
# TODO: make this getter work
# async def get_commands(dialog_manager: DialogManager, user_data: User, **kwargs) -> dict[str, str | None]:
#     pass
