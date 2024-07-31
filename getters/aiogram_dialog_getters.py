import html
from typing import Any

from aiogram.types import User
from aiogram.enums import ContentType

from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId

from lexicon.lexicon import LEXICON_COMMANDS
from services.service_functions import convert_dob


# getter for username
async def get_username(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict[str, str | None]:
    return {'username': html.escape(event_from_user.first_name)}


# TODO: refactor this getter
# getter for profile data
async def get_profile_data(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict[str, Any]:
    name = dialog_manager.dialog_data.get('name')
    gender = dialog_manager.dialog_data.get('gender')
    dob = convert_dob(dialog_manager.dialog_data.get('birthdate')) # type: ignore
    initial_weight = dialog_manager.dialog_data.get('initial_weight')
    
    if dialog_manager.dialog_data.get('initial_photo'):
        image_id = dialog_manager.dialog_data.get('initial_photo')
        initial_photo = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_id))  # type: ignore
        return {'name': html.escape(name), # type: ignore
                'gender': html.escape(gender), # type: ignore
                'date_of_birth': html.escape(dob),
                'initial_weight': initial_weight,
                'initial_photo': initial_photo}  # type: ignore
    else:
        return {'name': html.escape(name), # type: ignore
                'gender': html.escape(gender), # type: ignore
                'date_of_birth': html.escape(dob),
                'initial_weight': initial_weight}  # type: ignore


# getter for checking if there is initial photo in profile
async def get_init_photo(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict[str, Any]:
    initial_photo = dialog_manager.dialog_data.get('initial_photo')
    
    if initial_photo:
        return {}

    return {'initial_photo': 'empty'}


# getter for collecting all commands in one dict
# TODO: make this getter work
async def get_commands(**kwargs) -> dict[str, tuple]:
    commands = tuple([(k, v) for k, v in LEXICON_COMMANDS.items()])
    
    return {'commands': commands}
