import logging

from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)


# TODO: middleware for checking user is allowed
# TODO: rename middleware
# middleware for validating allowed users
class OuterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any]
    ) -> Any:
        logger.info(
            'We are in middleware %s, updaste type %s',
            __class__.__name__,
            event.__class__.__name__
        )
        
        result = await handler(event, data)
        
        logger.info('We are exiting middleware %s', __class__.__name__)
        
        return result
        

# TODO: middleware for filtering legit commands
