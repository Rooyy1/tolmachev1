from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import LEAD_NOTIFY_CHAT_ID
from data.storage import count_users

router = Router()


@router.message(Command("stats"))
async def cmd_stats(message: Message) -> None:
    """Просто число пользователей в боте. Доступно только @tema_evgenevich
    (чей chat_id указан в LEAD_NOTIFY_CHAT_ID) — остальным тихо игнорируется."""
    if LEAD_NOTIFY_CHAT_ID == 0 or message.chat.id != LEAD_NOTIFY_CHAT_ID:
        return
    await message.answer(str(count_users()))