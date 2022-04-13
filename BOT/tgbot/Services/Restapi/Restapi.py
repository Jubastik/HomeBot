# Функции запросов на rest api (использовать await!)
# Пока что просто затычки => фильтры работают через жопу, надо в коде указывать кем воспринимать юзеров
import json
import requests
import random
from CONSTANTS import URL_USER, URL_CLASS


# Tasks:
# !1) Реализация используемых фильтрами is_student, is_admin, is_developer
# 2) add_user


async def is_student(tguser_id):
    # есть ли в базе
    pass


async def is_unregistered(tguser_id):
    return not (await is_student(tguser_id))


async def is_admin(tguser_id):
    # админ или нет
    pass


async def is_developer(tguser_id):
    pass


# Вообще по хорошему создать вспомогательный класс для homework, так будет удобней и красивше.
async def add_homework(tguser_id, homework: dict):
    pass


def register_user(tguser_id, data):
    """Добавление юзера в бд к классу по ссылке, возвращает True если успешно, в противном случае False"""
    url_user = f"http://127.0.0.1:5000/api/user"
    # сначала регистрация полльзователя
    response = requests.post(
        url_user,
        json={
            "id": tguser_id,
            "platform": "tg",
            "class_token": data["class_id"],
            "name": data["name"],
        },
    )
    if response:
        return True
    else:
        return False


def register_class(tguser_id, data):
    """Добавление юзера в бд и создание класса, возвращает True если успешно, в противном случае False"""
    url_user = f"http://127.0.0.1:5000/api/user"
    url_class = f"http://127.0.0.1:5000/api/class"
    # сначала регистрация полльзователя
    response = requests.post(
        url_user, json={"id": tguser_id, "platform": "tg", "name": "Олег"}
    )
    print(response)
    if not response:
        return False
    # уже потом регистрация класса
    response = requests.post(
        url_class,
        json={"creator_platform": "tg", "creator_id": tguser_id, "name": "10A"},
    )
    if not response:
        return False

    return True
