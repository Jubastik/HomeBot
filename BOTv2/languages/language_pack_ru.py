from CONSTANTS import TG_BOT_LINK, TG_OFFICAL_CHANNEL


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

# Форматирование:
# <b>Жирный</b>
# <i>Курсив</i>
# <u>Подчеркнутый</u>
# <s>Зачеркнутый</s>
# <code>Моно</code>
# <a href='link'>Текс с ссылкой</a>


class LanguageRussian:
    empty = "{text}"
    by_link_success = "<i>Регистрация по ссылке успешна</i>"
    unexpected_message = "<i>P.S Пользуйся кнопками👇🏻</i>"
    wrong_class_token = "<i>Неверный формат код</i>"
    wrong_time = "<i>Неверный формат времени</i>"
    status_time_changed = "Время изменено⚡️"
    status_subject_added = "Предмет добавлен⚡️"
    shedule_stage = """
<b>{day_name}:</b>
{shedule}
"""

    warning = """
🚧<b>Бот находиться в бета-тесте</b>🚧
Поддержка: @Ru1kaa или @fohan
"""
    hello = """
Привет, давай зарегистрируем тебя!

<i>P.S. Бот находится в бета-тесте
Если что-то не работает, пиши @Ru1kaa или @fohan</i>
"""
    join_register_done = f"Подпишись на мой телеграм канал <b>{TG_OFFICAL_CHANNEL}</b>"
    start_time_check = """
Начало уроков в <i><b>{time}</b></i> по МСК

Чтобы изменить время, введи новое время в формате <b>ЧАСЫ:МИНУТЫ</b>

{status}
"""
    get_class_token = """
Введи <b>код</b> класса
<i>P.S. код есть у участников класса в профиле</i>

{status}
"""
    subjects_check = """
<b>Есть ли тут все твои школьные предметы?</b>

{subjects}

<i>P.S. Чтобы добавить предмет нужно отправить мне название в чат</i>👇🏻

<b>{status}</b>
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
    u_are_banned = "Ты забанен в этом классе"
    class_not_found = "Класс с таким кодом не найден"
    register_done1 = f"""
<b>Я зарегистрировал тебя</b>, теперь давай пригласим твоих одноклассников😉

Ссылка - <code>{TG_BOT_LINK}""" + """{token}</code>
"""
    register_done2 = f"""
Подключим "Петербургское образование"? Тогда я смогу показывать домашнее задание из него⚡️

P.S.Подпишись на мой телеграм канал <b>{TG_OFFICAL_CHANNEL}</b>🥺🥺🥺"""
    profile = """
<i><b>Профиль:</b></i>
Имя - <b>{name}</b>
ЭД: <b>{parser_status}</b>
Админ - {is_admin}
Ссылка приглашение - <code>""" + TG_BOT_LINK + """{class_token}</code>
Код класса - <code>{class_token}</code>
Админы класса - <b>{admins}</b>
"""
    spb_diary_get_login = '''
Введи <b>Email</b> от "Петербургского Образования"

<i>P.S. Мы не храним логин и пароль. Мы используем их лишь единожды для авторизации</i>😉
'''
    spb_diary_get_password = '''
Введи <b>пароль</b> от "Петербургского Образования"'''

    delete_account = "Ты уверен что хочешь удалить аккаунт?🥺"
    homework_history_dates = "Выбери дату👇🏻"

    class_panel = """
<b>Панель администратора⭐️</b>
<i>{status}</i>
"""
    admin_added = "Администратор добавлен"
    user_kicked = "Пользователь исключен из класса"
    choose_classmate = "Выбери одноклассника:"
    token_changed = "Код класса изменен - {token}⚡️"
    empty_ban_list = "Нету забаненых пользователей"
    user_unbanned = "Пользователь {name} разбанен"
    no_classmates = "Нету одноклассников"
    no_classmates_to_ban = "Некого банить"
    no_banned_users = "Нету забаненых пользователей"
    user_banned = "Пользователь {name} забанен"
    no_chats = """
Добавь бота в беседу класса и пропиши /start, чтобы запустить рассылку🙃
"""
    mailings_enabled = """
✉️Рассылки <b>включены</b>
Время отправки: <b>{time}</b>
"""
    mailings_disabled = """
✉️Рассылки <b>выключены</b>
Время отправки: <b>{time}</b>
"""
    status_mailings_enabled = "✉️Рассылки <b>включены</b>"
    status_mailings_disabled = "✉️Рассылки <b>выключены</b>"
    enter_time = "Введи время отправки в формате - <b>часы:минуты</b>"
    status_time_incorrect = "Время введено <b>неправильно</b>, попробуй ещё раз😉"
    # status_time_changed = "Время отправки изменено - <b>{time}</b>"
    no_assignable_admins = "Некого назначать администратором"
    choose_action = "Выбери действие:"
    chat_registered = """
<i>Чат зарегистрирован</i>
<b>/menu</b> - для перехода в меню
Зарегистрируйся по ссылке, чтобы добавлять домашку⚡️ {link} 
"""
    chat_unregistered = "Чтобы зарегистрировать чат, нужно зарегистрироватсья в <b>@homework_hub_bot</b>"
    homework_menu = "<b><i>Меню получения домашки</i></b>"
    date_menu = "На какой день ты хочешь получить домашку?🧐"
    homework_txt = """
<b>{subject} от {author}</b>

{txt}

<b><i>{info}</i></b>
"""

    choose_homework = "<b><i>Меню добавления домашки</i></b>"
    choose_subject = "Выбери предмет📕"
    choose_date = "Выбери день📅"
    choose_subject_on_date = "Выбери предмет из расписания на {date}📕"
    send_homework = """
<b>{date} {subject}</b>
Отправь домашку текстом или фоткой👇🏻
"""
    no_hw = "Ты мне ничего не отправил😭😭😭"
    check_hw = """
Записываю домашнее задание на {subject}?📌"""
    help_txt = """
<b>Бот находиться в разработке</b>
<i>Если у тебя возникли проблемы или есть пожелания пиши сюда:</i> @Ru1kaa или @fohan
"""