import logging
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Юзернейм тренера — сюда ведёт кнопка "Написать мне для оплаты" на карточке
# товара (deep-link вида https://t.me/<username>?text=...). Указывайте БЕЗ "@".
TRAINER_USERNAME = os.getenv("TRAINER_USERNAME", "Tolmachev92")

# chat_id тренера в Telegram — используется для служебных целей: проверка
# прав на команды /broadcast и /stats.
# Telegram Bot API не умеет слать сообщения "по юзернейму" — нужен числовой
# chat_id. Получить его просто:
#   1. Тренер открывает бота и пишет ему /whoami
#   2. Бот присылает его chat_id
#   3. Этот chat_id вписывается сюда, в .env
TRAINER_CHAT_ID = int(os.getenv("TRAINER_CHAT_ID", "0") or 0)

# Кому шлём уведомления о новых лидах (первый /start от пользователя).
# Юзернейм нужен только для человекочитаемых логов.
LEAD_NOTIFY_USERNAME = os.getenv("LEAD_NOTIFY_USERNAME", "tema_evgenevich")

# chat_id получателя уведомлений о лидах. Если 0 — уведомления не шлются.
LEAD_NOTIFY_CHAT_ID = int(os.getenv("LEAD_NOTIFY_CHAT_ID", "0") or 0)

# file_id фотографии для приветственного сообщения (/start).
# ВНИМАНИЕ: file_id привязан к конкретному боту, который изначально принял
# это фото. Если используется другой BOT_TOKEN — file_id может не сработать,
# в этом случае бот тихо отправит приветствие без фото (см. handlers/start.py).
WELCOME_PHOTO_ID = os.getenv(
    "WELCOME_PHOTO_ID",
    "AgACAgIAAxkBAAM0aqK7uYmInWFEOHTNSUhYMH59DQwAAisiaxv56hhJWtpja2bcWpoBAAMCAAN5AAM9BA",
)

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN не задан. Скопируйте .env.example в .env и укажите токен, "
        "полученный у @BotFather."
    )

if not TRAINER_CHAT_ID:
    logging.getLogger(__name__).warning(
        "TRAINER_CHAT_ID не задан — команды /broadcast и /stats будут недоступны. "
        "Попросите тренера написать боту /whoami и впишите chat_id в .env"
    )

if not LEAD_NOTIFY_CHAT_ID:
    logging.getLogger(__name__).warning(
        "LEAD_NOTIFY_CHAT_ID не задан — уведомления о новых лидах отправляться "
        "не будут. Попросите @%s написать боту /whoami и впишите chat_id в .env",
        LEAD_NOTIFY_USERNAME,
    )