import asyncio
import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from config import TRAINER_CHAT_ID
from data.storage import get_all_users
from data.texts import (
    BROADCAST_ASK_TEXT,
    BROADCAST_CANCELLED_TEXT,
    BROADCAST_DONE_TEXT,
    BROADCAST_STARTED_TEXT,
)

router = Router()
logger = logging.getLogger(__name__)


class Broadcast(StatesGroup):
    waiting_content = State()


def _is_trainer(message: Message) -> bool:
    """Команда доступна только тренеру — сверяем chat_id из .env.
    Если TRAINER_CHAT_ID не настроен, команда недоступна никому."""
    return TRAINER_CHAT_ID != 0 and message.chat.id == TRAINER_CHAT_ID


@router.message(Command("broadcast"))
async def cmd_broadcast(message: Message, state: FSMContext) -> None:
    if not _is_trainer(message):
        return  # обычным пользователям тихо игнорируем — это не для них
    await state.set_state(Broadcast.waiting_content)
    await message.answer(BROADCAST_ASK_TEXT)


@router.message(Command("cancel"), Broadcast.waiting_content)
async def cmd_cancel_broadcast(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(BROADCAST_CANCELLED_TEXT)


@router.message(Broadcast.waiting_content)
async def do_broadcast(message: Message, state: FSMContext) -> None:
    """Что бы тренер ни прислал (текст/фото/видео/документ) — рассылаем
    это же сообщение как копию каждому пользователю из базы."""
    if not _is_trainer(message):
        return
    await state.clear()

    users = get_all_users()
    total = len(users)
    status = await message.answer(BROADCAST_STARTED_TEXT.format(total=total))

    sent = 0
    failed = 0
    for user_id in users:
        if user_id == TRAINER_CHAT_ID:
            continue
        try:
            await message.copy_to(chat_id=user_id)
            sent += 1
        except Exception:
            logger.warning("Не удалось отправить рассылку пользователю %s", user_id)
            failed += 1
        await asyncio.sleep(0.05)  # ~20 сообщений/сек — с запасом от лимитов Telegram

    await status.edit_text(
        BROADCAST_DONE_TEXT.format(sent=sent, failed=failed, total=total)
    )
