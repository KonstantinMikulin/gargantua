import logging

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)


# TODO: middleware for checking user is allowed
# TODO: rename middleware
# middleware for validating allowed users
class MyOuterMiddleware(BaseMiddleware):
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
        
        result = await handler(event, data)
        
        logger.info('We are exiting middleware %s', __class__.__name__)
        
        return result
        

# TODO: middleware for filtering legit commands
