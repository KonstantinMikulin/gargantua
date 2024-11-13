import logging

from typing import Any, Awaitable, Callable, Dict, cast

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message

from cachetools import TTLCache # type:ignore

from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.requests import upsert_user

logger = logging.getLogger(__name__)


class TrackAllUsersMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.cache = TTLCache(
            maxsize=1000,
            ttl=60 * 60 * 6
        )
        
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        event = cast(Message, event)
        user_id = event.from_user.id # type:ignore
        
        # update user`s data if user not in cache
        if user_id not in self.cache:
            session: AsyncSession = data['session']
            await upsert_user(
                session=session,
                telegram_id=event.from_user.id,  # type:ignore
                first_name=event.from_user.first_name,  # type:ignore
                last_name=event.from_user.last_name,  # type:ignore
            )
            self.cache[user_id] = None
        
        return await handler(event, data)