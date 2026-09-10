"""Простое хранилище пользователей бота — для рассылки, статистики и
уведомлений о новых лидах.

Никакой базы данных не заводим: пользователей у бота немного, а JSON-файл
рядом с ботом проще разворачивать и не требует лишних зависимостей.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List

logger = logging.getLogger(__name__)

_STORAGE_PATH = Path(__file__).resolve().parent.parent / "users.json"


def _load() -> Dict[str, dict]:
    if not _STORAGE_PATH.exists():
        return {}
    try:
        with _STORAGE_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        logger.warning("Не удалось прочитать %s, начинаю с пустого списка.", _STORAGE_PATH)
        return {}

    # Совместимость со старым форматом, где лежал просто список id: [123, 456]
    if isinstance(data, list):
        return {str(uid): {} for uid in data}
    return data


def _save(users: Dict[str, dict]) -> None:
    with _STORAGE_PATH.open("w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)


def add_user(user) -> bool:
    """Сохраняет пользователя. Возвращает True, если он новый (первый раз
    пишет боту). Для уже известных пользователей просто возвращает False."""
    users = _load()
    uid = str(user.id)
    is_new = uid not in users
    if is_new:
        users[uid] = {
            "first_seen": datetime.utcnow().isoformat(timespec="seconds"),
            "username": user.username,
            "full_name": user.full_name,
        }
        _save(users)
    return is_new


def get_all_users() -> List[int]:
    """Список chat_id всех, кто хоть раз писал боту — нужен для рассылки."""
    return [int(uid) for uid in _load().keys()]


def count_users() -> int:
    """Всего пользователей в базе — для /stats."""
    return len(_load())