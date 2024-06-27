from time import sleep
import logging

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Chat

from lexicon.lexicon import LEXICON_COMMANDS, LEXICON_MIDDLEWARES

logger = logging.getLogger(__name__)


# TODO: check this middleware. It should be in first layer of middlewares.
# middleware for validating allowed users
class UserValidationOuterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        
        logger.info(
            'We are in middleware %s, update type %s',
            __class__.__name__,
            event.__class__.__name__
        )
        
        user_id: int = data.get('event_from_user').id # type: ignore
        allowed_users: list = data.get('config').tg_bot.users_ids # type: ignore
        bot: Bot = data.get('bot') # type: ignore
        user_chat: Chat = data.get('event_chat') # type: ignore
        
        if user_id not in allowed_users:
            logger.info('We are exiting middleware %s', __class__.__name__)
            await bot.send_message(
                chat_id=user_chat.id,
                # TODO: change this text
                text='You are not allowed'
            )
            
            return
    
        logger.info('We are exiting middleware %s', __class__.__name__)
        
        return await handler(event, data)
        
        
# middleware for admins
class AdminOuterMiddleware(BaseMiddleware):
    async def __call__(
    self,
    handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
    event: TelegramObject,
    data: Dict[str, Any]
    ) -> Any:
        
        logger.info(
            'We are in middleware %s, update type %s',
            __class__.__name__,
            event.__class__.__name__
        )
        
        user_id: int = data.get('event_from_user').id
        admins_ids: list = data.get('config').tg_bot.admin_ids
        
        if user_id in admins_ids:
            logger.info('We are exiting middleware %s', __class__.__name__)
            
            return await handler(event, data)
            
        return await handler(event, data)
    