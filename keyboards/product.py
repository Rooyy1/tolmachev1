from urllib.parse import quote

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import TRAINER_USERNAME
from data.products import PRODUCTS


def product_keyboard(key: str) -> InlineKeyboardMarkup:
    """Вместо реквизитов и подтверждения оплаты внутри бота — сразу ведём
    клиента в личку к тренеру. Сообщение в чате уже предзаполнено названием
    товара, чтобы тренер сразу понимал, что человек хочет обсудить."""
    title = PRODUCTS[key]["title"]
    prefill = quote(f"Привет Никита, хочу обсудить {title}")

    builder = InlineKeyboardBuilder()
    builder.button(
        text="✍️ Написать мне для оплаты",
        url=f"https://t.me/{TRAINER_USERNAME}?text={prefill}",
    )
    builder.button(text="⬅️ Назад", callback_data="back_main")
    builder.adjust(1)
    return builder.as_markup()
