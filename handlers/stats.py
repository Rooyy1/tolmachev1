from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import TRAINER_CHAT_ID
from data.storage import count_users

router = Router()


@router.message(Command("stats"))
async def cmd_stats(message: Message) -> None:
    """Просто число пользователей в боте. Доступно только тренеру —
    остальным команда тихо игнорируется."""
    if TRAINER_CHAT_ID == 0 or message.chat.id != TRAINER_CHAT_ID:
        return
    await message.answer(str(count_users()))