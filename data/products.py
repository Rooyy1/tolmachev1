"""Каталог продуктов Никиты Толмачёва.

Чтобы поменять цену, название или описание товара — правьте только этот
файл, весь остальной код тянет данные отсюда.

"""

CATEGORIES = {
    "cat_split": {
        "title": "🏋️ Программы тренировок",
        "desc": "Индивидуальная программа тренировок, рассчитана на месяц. Выбери формат сплита:",
        "products": ["split_3", "split_4"],
    },
    "cat_split_ddx": {
        "title": "💊 Программы тренировок под DDX",
        "desc": "Та же индивидуальная программа, адаптированная под приём DDX. Выбери формат сплита:",
        "products": ["split_3_ddx", "split_4_ddx"],
    },
    "cat_nutrition": {
        "title": "🥗 Планы питания",
        "desc": "Индивидуальный план питания под твою цель:",
        "products": ["nutrition_mass", "nutrition_cut"],
    },
    "cat_combo": {
        "title": "🔥 Тренировки + питание",
        "desc": "Сплит на 3–4 дня и план питания в одном пакете:",
        "products": ["combo_mass", "combo_cut"],
    },
    "cat_consult": {
        "title": "💬 Консультации",
        "desc": "Разовая консультация под конкретный запрос:",
        "products": ["consult_pharma", "consult_plate", "consult_complex"],
    },
    "cat_online": {
        # У этой категории отдельный длинный текст с чек-листом — см. texts.ONLINE_INTRO
        "title": "📲 Онлайн-ведение",
        "desc": None,
        "products": ["online_1m", "online_3m", "online_6m", "online_12m"],
    },
}

PRODUCTS = {
    # ---------- Программы тренировок ----------
    "split_3": {
        "title": "3-дневный сплит",
        "price": 2990,
        "category": "cat_split",
        "photo": "AgACAgIAAxkBAAMaaqKsiqFFWlvrRa8kb6xx9xiEwh0AArchaxv56hhJBw495I-M-lUBAAMCAAN5AAM9BA",
        "short": "Индивидуальная программа тренировок на 3 дня в неделю, рассчитана на месяц.",
    },
    "split_4": {
        "title": "4-дневный сплит",
        "price": 2990,
        "category": "cat_split",
        "photo": "AgACAgIAAxkBAAMeaqKsj5gSBqoCue_vFA7jFWtjGwcAArkhaxv56hhJQKF27Z1nt0wBAAMCAAN5AAM9BA",
        "short": "Индивидуальная программа тренировок на 4 дня в неделю, рассчитана на месяц.",
    },
    # ---------- Программы тренировок под DDX ----------
    "split_3_ddx": {
        "title": "3-дневный сплит под DDX",
        "price": 2990,
        "category": "cat_split_ddx",
        "photo": "AgACAgIAAxkBAAMYaqKsiUfAI9R1pTQL0quc5GEpEmQAArYhaxv56hhJfW62OF467M4BAAMCAAN5AAM9BA",
        "short": "Индивидуальная программа на 3 дня в неделю, адаптированная под приём DDX. Рассчитана на месяц.",
    },
    "split_4_ddx": {
        "title": "4-дневный сплит под DDX",
        "price": 2990,
        "category": "cat_split_ddx",
        "photo": "AgACAgIAAxkBAAMcaqKsjWP_H1bg_smb9qvSC2tNCUcAArghaxv56hhJ5aTqpM6070UBAAMCAAN5AAM9BA",
        "short": "Индивидуальная программа на 4 дня в неделю, адаптированная под приём DDX. Рассчитана на месяц.",
    },
    # ---------- Планы питания ----------
    "nutrition_mass": {
        "title": "План питания на массу",
        "price": 4500,
        "category": "cat_nutrition",
        "photo": "AgACAgIAAxkBAAMUaqKsg1I1TSVIhQSBHAIsuvEGL-QAArQhaxv56hhJs_iqeHexAaMBAAMCAAN5AAM9BA",
        "short": "Индивидуальный план питания для набора качественной мышечной массы.",
    },
    "nutrition_cut": {
        "title": "План питания на жиросжигание",
        "price": 4500,
        "category": "cat_nutrition",
        "photo": "AgACAgIAAxkBAAMSaqKsgBHxjd3lhzu6_FuJlQ5sNc8AArMhaxv56hhJVuOOEIlKUd0BAAMCAAN5AAM9BA",
        "short": "Индивидуальный план питания для снижения жировой массы без потери мышц.",
    },
    # ---------- Тренировки + питание ----------
    "combo_mass": {
        "title": "3-4х дневный сплит + питание на массу",
        "price": 5990,
        "category": "cat_combo",
        "photo": "AgACAgIAAxkBAAMCaqKs1um_2OXn9x6k0o7p_70MLn0AAr4haxv56hhJ-XzSpjbLhmABAAMCAAN5AAM9BA",
        "short": "Программа тренировок (3-4 дня в неделю) и план питания для набора массы — единый пакет.",
    },
    "combo_cut": {
        "title": "3-4х дневный сплит + питание на сброс веса",
        "price": 5990,
        "category": "cat_combo",
        "photo": "AgACAgIAAxkBAAMEaqKsbiU16oZYFPcb3oOqY1CaRFUAAqwhaxv56hhJUaO3mHffjecBAAMCAAN5AAM9BA",
        "short": "Программа тренировок (3-4 дня в неделю) и план питания для снижения веса — единый пакет.",
    },
    # ---------- Консультации ----------
    "consult_pharma": {
        "title": "Консультация по фарме",
        "price": 2500,
        "category": "cat_consult",
        "photo": "AgACAgIAAxkBAAMIaqKsdL_DvkJ8WHU-oVKXtLGP5pUAAq4haxv56hhJ3-bqtbsyJnQBAAMCAAN5AAM9BA",
        "short": "Дозировки, анализы, подбор в аптеке — индивидуальный разбор твоей ситуации.",
    },
    "consult_plate": {
        "title": "Разбор твоей тарелки",
        "price": 2500,
        "category": "cat_consult",
        "photo": "AgACAgIAAxkBAAMWaqKshhB-9lstnHc6AzcmWUb-gMIAArUhaxv56hhJ6excIOqKbIEBAAMCAAN5AAM9BA",
        "short": "Полный разбор твоего текущего питания и рекомендации по корректировке.",
    },
    "consult_complex": {
        "title": "Комплекс: питание + трени + фарма + добавки",
        "price": 4500,
        "category": "cat_consult",
        "photo": "AgACAgIAAxkBAAMGaqKscAhaf13sBkh4TcaZY2tTio4AAq0haxv56hhJAtZt8g1Y9NEBAAMCAAN5AAM9BA",
        "short": "Комплексная консультация: питание, тренировки, фармакология и спортивное питание.",
    },
    # ---------- Онлайн-ведение ----------
    "online_1m": {
        "title": "Онлайн-ведение — 1 месяц",
        "price": 10990,
        "category": "cat_online",
        "photo": "AgACAgIAAxkBAAMMaqKseWIpAAH8P9V29y3udjCm2r_mAAKwIWsb-eoYSSNiwPNpMSogAQADAgADeQADPQQ",
        "short": "Полное онлайн-ведение на 1 месяц (состав — см. описание выше).",
    },
    "online_3m": {
        "title": "Онлайн-ведение — 3 месяца",
        "price": 27990,
        "category": "cat_online",
        "photo": "AgACAgIAAxkBAAMOaqKse6BxE84dDGvHnUx9n6ofHXAAArEhaxv56hhJ5Ucyz61IEXYBAAMCAAN5AAM9BA",
        "short": "Полное онлайн-ведение на 3 месяца (состав — см. описание выше).",
    },
    "online_6m": {
        "title": "Онлайн-ведение — 6 месяцев",
        "price": 50000,
        "category": "cat_online",
        "photo": "AgACAgIAAxkBAAMQaqKsfhBCGHOjb4OWNRMrN891BEQAArIhaxv56hhJGKtu3CFmzIwBAAMCAAN5AAM9BA",
        "short": "Полное онлайн-ведение на 6 месяцев (состав — см. описание выше).",
    },
    "online_12m": {
        "title": "Онлайн-ведение — 12 месяцев",
        "price": 95000,
        "category": "cat_online",
        "photo": "AgACAgIAAxkBAAMKaqKsd8bJQOqHuD-ij1TDjuZxzQoAAq8haxv56hhJxQEMqP-x2swBAAMCAAN5AAM9BA",
        "short": "Полное онлайн-ведение на 12 месяцев (состав — см. описание выше).",
    },
}


def format_price(price: int) -> str:
    return f"{price:,}".replace(",", " ") + " ₽"


def build_product_card(key: str) -> str:
    p = PRODUCTS[key]
    return f"<b>{p['title']}</b>\n💰 {format_price(p['price'])}\n\n{p['short']}"
