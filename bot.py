import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ErrorEvent

from config import BOT_TOKEN
from handlers import broadcast, catalog, common, start, stats
from middlewares.track_user import TrackUserMiddleware

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    # Запоминаем каждого, кто написал боту, — нужно для рассылки и статистики.
    dp.update.outer_middleware(TrackUserMiddleware())

    # Порядок важен: специфичные роутеры — раньше общего fallback-обработчика.
    dp.include_router(start.router)
    dp.include_router(catalog.router)
    dp.include_router(broadcast.router)
    dp.include_router(stats.router)
    dp.include_router(common.router)  # ловит всё, что не подошло другим роутерам

    @dp.error()
    async def error_handler(event: ErrorEvent) -> None:
        logger.exception(
            "Ошибка при обработке апдейта %s: %s", event.update, event.exception
        )

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        logger.info("Бот запущен, начинаю polling...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Бот остановлен.")