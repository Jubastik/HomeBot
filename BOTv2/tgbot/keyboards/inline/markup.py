from aiogram.types import InlineKeyboardButton
import aiogram.types as types
from tgbot.keyboards.inline.callback_data import (
    ArrowsData,
    CheckHomework,
    DatesData,
    StudentsData,
    SubjectData,
)


class InlineKeyboardMarkup(types.InlineKeyboardMarkup):
    def __call__(self, *args, **kwargs):
        return self


# | RegistrationManager | RegistrationManager | RegistrationManager | RegistrationManager | RegistrationManager | RegistrationManager |
DEFAULT_REGISTRATION = [
    InlineKeyboardButton(text="< Назад", callback_data="back"),
    InlineKeyboardButton(text="Дальше >", callback_data="next"),
]


markup_registration_default = InlineKeyboardMarkup(inline_keyboard=[DEFAULT_REGISTRATION])

markup_subjects_stage = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Удалить добавленный предмет", callback_data="remove")],
        DEFAULT_REGISTRATION,
    ]
)


def get_markup_shedule_stage(subjects, last_day=False):
    keyboard = InlineKeyboardMarkup(
        row_width=3,
    )
    keyboard.insert(InlineKeyboardButton(text="Вверх ↑", callback_data=ArrowsData.new(num=-1)))
    keyboard.insert(InlineKeyboardButton(text="Удалить", callback_data="remove"))
    keyboard.insert(InlineKeyboardButton(text="Вниз ↓", callback_data=ArrowsData.new(num=1)))
    for subject in subjects:
        keyboard.insert(InlineKeyboardButton(text=subject, callback_data=SubjectData.new(name=subject)))
    if last_day:
        keyboard.add(InlineKeyboardButton(text="< Назад", callback_data="back"))
    else:
        keyboard.add(*DEFAULT_REGISTRATION)
    keyboard.add(InlineKeyboardButton(text="Зарегистрироваться", callback_data="register"))
    return keyboard


markup_join_by_id_stage = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="next")]]
)

markup_next = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Далее", callback_data="next")]])

markup_register_done2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подключить ЭД", callback_data="connect_diary")],
        [InlineKeyboardButton(text="Завершить регистрацию", callback_data="next")],
    ]
)


# | Registration | Registration | Registration | Registration | Registration | Registration | Registration | Registration |


markup_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Присоедениться", callback_data="back"),
            InlineKeyboardButton(text="Создать класс", callback_data="next"),
        ],
    ]
)

markup_back = InlineKeyboardMarkup(inline_keyboard=[InlineKeyboardButton(text="Назад", callback_data="back")])

markup_yes_or_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data="check_true"),
            InlineKeyboardButton(text="Нет", callback_data="check_false"),
        ],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)

markup_check_subjects1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Продолжить", callback_data="Check_Subjects_okey")],
        [InlineKeyboardButton(text="Отмена действия", callback_data="Check_Subjects_undo")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)
markup_shedule2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Готово", callback_data="shedule_done")]]
)


def get_markup_shedule(subjects) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)
    for i in range(len(subjects)):
        keyboard.insert(
            InlineKeyboardButton(
                text=subjects[i],
                callback_data=SubjectData.new(name=subjects[i]),
            )
        )
    keyboard.add(
        InlineKeyboardButton(text="Вверх⬆️", callback_data=ArrowsData.new(num=-1)),
        InlineKeyboardButton(text="Вниз⬇️", callback_data=ArrowsData.new(num=1)),
    )
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data="back"))
    return keyboard


# | Student | Student | Student | Student | Student | Student | Student | Student |


def markup_profile(is_admin, parser_status=0):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Меню", callback_data="menu")],
        ]
    )
    if parser_status == 0 or parser_status == 2:
        markup.add(
            InlineKeyboardButton(text='Подключить "Петербургское Образование"', callback_data="connect_spb_diary")
        )
    else:
        markup.add(
            InlineKeyboardButton(text='Отключить "Петербургское Образование"', callback_data="disable_spb_diary")
        )
    markup.add(InlineKeyboardButton(text="История домашки", callback_data="get_homework_history"))
    if is_admin:
        markup.add(InlineKeyboardButton(text="Управление классом", callback_data="class_management"))
    markup.add(InlineKeyboardButton(text="Удалить аккаунт", callback_data="delete_account"))
    return markup


markup_add_homework = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Быстро добавить", callback_data="fast_add")],
        [InlineKeyboardButton(text="Добавить на дату", callback_data="on_date_add")],
        [InlineKeyboardButton(text="Меню", callback_data="menu")],
    ]
)


def get_markup_student_menu(subjects=[]) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    for subject in subjects:
        keyboard.insert(InlineKeyboardButton(text=subject))
    keyboard.add(
        InlineKeyboardButton(text="Добавить дз📌", callback_data="add_homework"),
        InlineKeyboardButton(text="Дз на завтра⚡️", callback_data="get_next_date_hw"),
    )
    keyboard.add(
        InlineKeyboardButton(text="Добавить дз на дату📆", callback_data="add_on_date"),
        InlineKeyboardButton(text="Получить дз🔍", callback_data="get_homework"),
    )
    keyboard.add(InlineKeyboardButton(text="Моё расписание📚", callback_data="my_shedule"))
    keyboard.add(InlineKeyboardButton(text="Профиль👤", callback_data="profile"))

    return keyboard


markup_check_homework = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Да, все верно", callback_data=CheckHomework.new(boolean="true"))],
        [InlineKeyboardButton(text="Нет", callback_data=CheckHomework.new(boolean="false"))],
    ]
)
markup_done = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Готово", callback_data="done")],
        [InlineKeyboardButton(text="Меню", callback_data="menu")],
    ]
)


def get_markup_dates(dates):
    keyboard = InlineKeyboardMarkup(row_width=3)
    for date in dates:
        keyboard.insert(
            InlineKeyboardButton(
                text=date[0],
                callback_data=DatesData.new(date=date[1]),
            )
        )
    keyboard.add(InlineKeyboardButton(text="Меню", callback_data="menu"))
    return keyboard


def get_subjects_markup(subjects):
    keyboard = InlineKeyboardMarkup(row_width=3)
    for i in subjects:
        keyboard.insert(
            InlineKeyboardButton(
                text=i,
                callback_data=SubjectData.new(name=i),
            )
        )
    keyboard.add(InlineKeyboardButton(text="Меню", callback_data="menu"))
    return keyboard


markup_are_u_sure = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Да", callback_data="true")],
        [InlineKeyboardButton(text="Отмена", callback_data="menu")],
    ]
)

markup_get_homework = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="На завтра", callback_data="fast_get")],
        [InlineKeyboardButton(text="На дату", callback_data="on_date_get")],
        [InlineKeyboardButton(text="Меню", callback_data="menu")],
    ]
)
markup_menu = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Вернуться в меню", callback_data="menu")]]
)


markup_error_menu = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Вернуться в меню", callback_data="error_menu")]]
)


markup_class_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        # [InlineKeyboardButton(text="Рассылка", callback_data="mailing")],
        [InlineKeyboardButton(text="Сменить токен", callback_data="remove_token")],
        [InlineKeyboardButton(text="Добавить администратора", callback_data="add_admin")],
        [InlineKeyboardButton(text="Разбанить одноклассника", callback_data="unban")],
        [InlineKeyboardButton(text="Забанить одноклассника", callback_data="ban")],
        [InlineKeyboardButton(text="Меню", callback_data="menu")],
    ]
)


markup_mailing_disabled = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Изменить время рассылки", callback_data="change_time")],
        [InlineKeyboardButton(text="Включить рассылку", callback_data="enable_mailing")],
        [InlineKeyboardButton(text="Меню", callback_data="menu")],
    ]
)

markup_mailing_enabled = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Изменить время рассылки", callback_data="change_time")],
        [InlineKeyboardButton(text="Отключить рассылку", callback_data="disable_mailing")],
        [InlineKeyboardButton(text="Меню", callback_data="menu")],
    ]
)


markup_back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back")]])


def get_markup_classmates(data):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for mate in data:
        keyboard.insert(
            InlineKeyboardButton(
                text=mate["name"],
                callback_data=StudentsData.new(tguser_id=mate["tg_id"], name=mate["name"]),
            )
        )
    keyboard.add(InlineKeyboardButton(text="Меню", callback_data="menu"))
    return keyboard

def get_markup_banned_users(data):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for mate in data:
        keyboard.insert(
            InlineKeyboardButton(
                text=mate["name"],
                callback_data=StudentsData.new(tguser_id=mate["id"], name=mate["name"]),
            )
        )
    keyboard.add(InlineKeyboardButton(text="Меню", callback_data="menu"))
    return keyboard


# | Developer | Developer | Developer | Developer | Developer | Developer | Developer | Developer |


markup_developer_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Рассылка", callback_data="mailing")],
        [InlineKeyboardButton(text="Отправить сообщение", callback_data="mail_to")],
    ]
)

markup_developer_deny = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Отмена", callback_data="deny")]]
)

markup_developer_mailingcheck = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать рассылку", callback_data="start_mailing")],
        [InlineKeyboardButton(text="Отмена", callback_data="deny")],
    ]
)
makrup_group_menu = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Получить домашку", callback_data="get_homework")]]
)
