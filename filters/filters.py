import logging

from aiogram import Bot
from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)

class UserValidation(BaseFilter):
    async def __call__(self, event: TelegramObject, config, bot: Bot) -> bool:
        logger.info('We are inside filter %s', __class__.__name__)
        allowed_users = config.tg_bot.users_ids
        
        if event.from_user.id in allowed_users: # type: ignore
            return True
        
        else:
            await bot.send_message(chat_id=event.chat.id, text='You are not allowed') # type: ignore
            return False
