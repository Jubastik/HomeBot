import os

SUBJECTS = [
    "Русский🇷🇺",
    "Литература📚",
    "Алгебра🔢",
    "Геометрия📐",
    "Биология🌿",
    "География🌐",
    "История🗿",
    "Право⚖️",
    "Химия🧪",
    "Физкультура⚽️",
    "English🇬🇧",
    "Физика⚡️",
    "Информатика📡",
]
SERVER = os.getenv("TG_API_SERVER") # при работе с url в следующий раз, сделать рефактор
URL_USER = SERVER + '/api/user'
URL_CHAT = SERVER + '/api/chats'
URL_CLASS = SERVER + '/api/class'
URL_SCHEDULE = SERVER + '/api/schedule'
URL_HOMEWORK = SERVER + '/api/homework'
URL_TIME_TABLE = SERVER + '/api/time_table'
URL_CURRENT_LESSONS = SERVER + '/api/current_lessons'
WEEKDAYS = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница',
            5: 'суббота', 6: 'воскресенье'}
