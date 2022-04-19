from tgbot.services.restapi.restapi import is_lessons_in_saturday


def time_is_correct(time: list):
    try:
        hours, minutes = map(int, time.split(":"))
        if hours < 0 or minutes < 0 or hours > 24 or minutes > 60:
            return False
        if hours != hours or minutes != minutes:
            return False
        return [str(hours), str(minutes)]
    except:
        return False


def convert_time(time: list):
    if len(time[1]) == 1:
        time[1] = f"1{time[1]}"
    return time


def convert_position(pos):
    return [((pos) // 8), (pos % 8)]


def generate_dates() -> list:
    """Генерирует даты"""
    saturday_lesson = is_lessons_in_saturday()
    # Вот так вот если is_lessons_in_saturday() возвращает True для 19.04
    return [
        "20.04 Среда",
        "21.04 Четверг",
        "22.04 Пятница",
        "23.04 Суббота",
        "25.04 Понедельник",
        "26.04 Вторник",
    ]
