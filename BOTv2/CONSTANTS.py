import os

SUBJECTS = [
    "Русский🇷🇺",
    "Литература📚",
    "Алгебра🔢",
    "Геометрия📐",
    "Биология🌿",
    "География🌐",
    "История🗿",
    "Обществознание⚖",
    "Химия🧪",
    "Физкультура⚽",
    "English🇬🇧",
    "Физика⚡",
    "Информатика📡",
    "ОБЖ🪖",
    "Астрономия🔭",
    "Разговоры о важном🗣",
]
TG_BOT_LINK = "t.me/homework_hub_bot?start="
TG_OFFICAL_CHANNEL = "@Homework_bot_HUB"
API_TOKEN = os.getenv('API_TOKEN', 'root')
WEEKDAYS = {
    0: "понедельник",
    1: "вторник",
    2: "среда",
    3: "четверг",
    4: "пятница",
    5: "суббота",
    6: "воскресенье",
}
WEEKDAYS_TRASNLATE = {
    "понедельник": "monday",
    "вторник": "tuesday",
    "среда": "wednesday",
    "четверг": "thursday",
    "пятница": "friday",
    "суббота": "saturday",
    "воскресенье": "sunday",
}
