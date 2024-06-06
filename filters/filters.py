from aiogram.filters import BaseFilter
from aiogram.types import Message, TelegramObject

from lexicon.lexicon import LEXICON_COMMANDS


class UserValidation(BaseFilter):
    async def __call__(self, event: TelegramObject, config) -> bool:
        allowed_users = config.tg_bot.users_ids
        
        if event.from_user.id not in allowed_users: # type: ignore
            return True
        
        return False
