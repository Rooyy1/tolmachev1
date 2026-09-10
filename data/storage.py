"""Простое хранилище id пользователей бота — нужно только для рассылки.

Никакой базы данных не заводим: пользователей у бота немного, а JSON-файл
рядом с ботом проще разворачивать и не требует лишних зависимостей.
"""

import json
import logging
from pathlib import Path
from typing import Set

logger = logging.getLogger(__name__)

_STORAGE_PATH = Path(__file__).resolve().parent.parent / "users.json"


def _load() -> Set[int]:
    if not _STORAGE_PATH.exists():
        return set()
    try:
        with _STORAGE_PATH.open("r", encoding="utf-8") as f:
            return set(json.load(f))
    except (json.JSONDecodeError, OSError):
        logger.warning("Не удалось прочитать %s, начинаю с пустого списка.", _STORAGE_PATH)
        return set()


def _save(users: Set[int]) -> None:
    with _STORAGE_PATH.open("w", encoding="utf-8") as f:
        json.dump(sorted(users), f)


def add_user(user_id: int) -> None:
    """Добавить пользователя в базу для рассылки, если его там ещё нет."""
    users = _load()
    if user_id not in users:
        users.add(user_id)
        _save(users)


def get_all_users() -> Set[int]:
    return _load()
