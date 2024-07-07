import html
from typing import Any

from aiogram.types import User
from aiogram.enums import ContentType

from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId


# getter for username
async def get_username(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict[str, str | None]:
    return {'username': html.escape(event_from_user.first_name)}


# TODO: refactor this getter
# getter for profile data
async def get_profile_data(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict[str, Any]:
    name = dialog_manager.dialog_data.get('name')
    gender = dialog_manager.dialog_data.get('gender')
    
    try:
        dialog_manager.dialog_data.get('initial_photo')
    except KeyError:
        return {'name': html.escape(name), 'gender': html.escape(gender)}  # type: ignore
    else:
        image_id = dialog_manager.dialog_data.get('initial_photo')
        initial_photo = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_id))  # type: ignore
        
        return {'name': html.escape(name), 'gender': html.escape(gender), 'initial_photo': initial_photo}  # type: ignore


# getter for collecting all commands in one dict
# TODO: make this getter work
# async def get_commands(dialog_manager: DialogManager, user_data: User, **kwargs) -> dict[str, str | None]:
#     pass
