import logging

from aiogram.filters import BaseFilter
from aiogram.types import Message

logger = logging.getLogger(__name__)


# admin`s ID filter
class AdminIDFilter(BaseFilter):
    """
    Check User`s ID presence in list of admins
    """
        
    async def __call__(self, message: Message, config) -> bool:
        if message.from_user.id in config.tg_bot.admins_ids:
            return True
        
        return False
    