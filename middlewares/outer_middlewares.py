from time import sleep
import logging

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Chat

from lexicon.lexicon import LEXICON_COMMANDS, LEXICON_MIDDLEWARES

logger = logging.getLogger(__name__)


# TODO: cheak this middleware. It should be in first layer of middlewares.
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
        
        # TODO: remove this line
        data.update({'hey': 'Hello you!!!'})
        
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
        
        

# TODO: middleware for filtering legit commands
# middleware for filtering legit commands
class CommandsValidationOuterMiddleware(BaseMiddleware):
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

        bot: Bot = data.get('bot') # type: ignore
        user_chat: Chat = data.get('event_chat') # type: ignore
        bot_commands = data.get('commands')
        command = event.message.text # type: ignore
        
        if command not in bot_commands:
            # TODO: fix sending messages
            logger.info('We are exiting middleware %s', __class__.__name__)
            await bot.send_message(
                chat_id=user_chat.id,
                # TODO: change this text
                text=LEXICON_COMMANDS['wrong_cmd']
            )
            sleep(1)
            await bot.send_message(
                chat_id=user_chat.id,
                # TODO: change this text
                text=LEXICON_MIDDLEWARES['show_cmds']
            )
            
            return
            
        logger.info('We are exiting middleware %s', __class__.__name__)
        
        return await handler(event, data)
        