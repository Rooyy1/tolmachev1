from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from data.storage import add_user


class TrackUserMiddleware(BaseMiddleware):
    """Сохраняет chat_id каждого, кто прислал боту сообщение или нажал
    кнопку, — на этом строится рассылка (см. handlers/broadcast.py) и
    статистика (см. handlers/stats.py). Уведомление о новом лиде шлётся
    из /start (см. handlers/start.py), а не здесь, чтобы не спамить при
    каждом действии пользователя."""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user = data.get("event_from_user")
        if user is not None and not user.is_bot:
            add_user(user)
        return await handler(event, data)