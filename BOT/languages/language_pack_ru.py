class DayText:
    translate = {
        "monday": "Понедельник",
        "tuesday": "Вторник",
        "wednesday": "Среда",
        "thursday": "Четверг",
        "friday": "Пятница",
        "saturday": "Суббота",
    }

    def __init__(self) -> None:
        pass

    def format(self, **kwargs) -> str:
        res = ""
        for day, lessons in kwargs.items():
            res += f"<b>{self.translate[day]}:</b>\n"
            res += lessons + "\n"
        return res


class LanguageRussian:
    by_link_success = "<i>Регистрация по ссылке успешна</i>"
    warning = """
🚧<b>Бот находиться в бета-тесте</b>🚧
Поддержка: @Ru1kaa или @fohan
"""
    hello = """
Привет, давай зарегестрируем тебя!
<code>Присоедениться</code> - Для присоеденения к классу
<code>Создать класс</code> - Для создания нового класса"""
    start_time_check = "Твои уроки начинаются в <i><b>{time}</b></i>?"
    get_class_token = """
Введи <b>токен</b> класса
<i>P.S. Токен есть у участников класса в профиле</i>"""
    subjects_check = """
<b>Есть ли тут все твои школьные предметы?</b>

{subjects}

<code>Продолжить</code> - Для перехода на следующий этап регистрации
<code>Отмена действия</code> - Для удаления последнего предмета из списка
<code>Назад</code> - Для возврата на прошлый этап регистрации

<i>P.S. Чтобы добавить свой предмет нужно отправить мне его название в чат</i>👇🏻
"""
    shedule1 = """
<b>Понедельник:</b>
{monday}
<b>Вторник:</b>
{tuesday}
<b>Среда:</b>
{wednesday}
<b>Четверг:</b>
{thursday}
<b>Пятница:</b>
{friday}
<b>Суббота:</b>
{saturday}

<i>P.S. Как заполнишь расписание нажми кнопку <b>"Готово"</b>👇🏻</i>
"""
    shedule2 = """
Заполним расписание на неделю

<code>Вверх⬆️/Вниз⬇️</code> - Для изменения текущего предмета
<code>[Название предмета]</code> - Для добавления предмета в расписание
<code>Назад</code> - Для возврата на прошлый этап регистрации

<i>P.S. Перед тем, как добавить предмет, проверь что на кпопках нету часиков</i>
"""
    shedule3 = DayText()
    add_time = """
Введи время начала уроков в формате - <b>часы:минуты</b>
<i>Например "8:30"</i>
"""
    uncorrect_time = "Время введено <b>неправильно</b>, попробуй ещё раз😉"
    correct_time = "Записано время начала уроков - <i><b>{time}</b></i>"
    menu = "Меню"
    register_done = """
<b>Я зарегистрировал тебя</b>, теперь давай пригласим твоих одноклассников😉

Ссылка - <code>{link}{token}</code>

<i>P.S. Также можешь добавить меня в беседу своего класса, тогда все смогут получать домашку🙃</i>
"""
    register_done2 = "Подпишись на мой телеграм канал <b>{channel}</b>🥺🥺🥺"
    profile = """
<i><b>Профиль:</b></i>
Имя - <b>{name}</b>
Админ - {is_admin}
Ссылка приглашение - <code>{link}{class_token}</code>
Токен - <code>{class_token}</code>
Админы класса - <b>{admins}</b>
"""
    delete_account = "Ты уверен что хочешь удалить аккаунт?🥺"
    homework_history_dates = "Выбери дату👇🏻"

    class_panel = """
<b>Панель администратора⭐️</b>
<i>{status}</i>
"""
    admin_added = "Администратор добавлен"
    user_kicked = "Пользователь исключен из класса"
    choose_classmate = "Выбери одноклассника:"
    token_changed = "Токен изменен - <code>{token}</code>"
    empty_ban_list = "Нету забаненых пользователей"
    no_classmates = "Нету одноклассников"

    choose_action = "Выбери действие:"
    chat_registered = """
<i>Чат зарегистрирован</i>
<b>/menu</b> - для перехода в меню
Зарегистрируйся по ссылке, чтобы добавлять домашку⚡️ {link} 
"""
    chat_unregistered = "Чтобы зарегистрировать чат, нужно зарегистрироватсья в <b>@hw_assistant_bot</b>"
    homework_menu = "<b><i>Меню получения домашки</i></b>"
    date_menu = "На какой день ты хочешь получить домашку?🧐"
    homework_txt = """
<b>{subject} от {author}</b>

{txt}
"""

    choose_homework = "<b><i>Меню добавления домашки</i></b>"
    choose_subject = "Выбери предмет📕"
    choose_date = "На какой день ты хочешь добавить домашку?🧐"
    choose_subject_on_date = "Выбери предмет из расписания на {date}📕"
    send_homework = "Отправь домашку текстом или фоткой👇🏻"
    no_hw = "Ты мне ничего не отправил😭😭😭"
    check_hw = """
Записываю домашнее задание на {subject}?📌"""
    help_txt = """
<b>Бот находиться в разработке</b>
<i>Если у тебя возникли проблемы или есть пожелания пиши сюда:</i> @Ru1kaa или @fohan
"""


# Форматирование:
# <b>Жирный</b>
# <i>Курсив</i>
# <u>Подчеркнутый</u>
# <s>Зачеркнутый</s>
# <code>Моно</code>
# <a href='link'>Текс с ссылкой</a>
