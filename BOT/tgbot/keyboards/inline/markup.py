from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.inline.callback_data import (
    SubjectData,
    ArrowsData,
    CheckHomework,
    DatesData,
    StudentsData,
)


# | Registration | Registration | Registration | Registration | Registration | Registration | Registration | Registration |


markup_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Присоединиться к классу по id", callback_data="join_class_by_id"
            ),
            InlineKeyboardButton(text="Создать класс", callback_data="make_class"),
        ],
    ]
)

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
        [InlineKeyboardButton(text="Всё верно", callback_data="Check_Subjects_okey")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
)
markup_check_subjects2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отмена", callback_data="Check_Subjects_undo")],
    ]
)
markup_shedule2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Готово", callback_data="shedule_done")]
    ]
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
        InlineKeyboardButton(text="Вверх", callback_data=ArrowsData.new(num=-1)),
        InlineKeyboardButton(text="Вниз", callback_data=ArrowsData.new(num=1)),
    )
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data="back"))
    return keyboard


# | Student | Student | Student | Student | Student | Student | Student | Student |


markup_profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Меню", callback_data="menu")],
        [InlineKeyboardButton(text="Удалить аккаунт", callback_data="delete_account")],
    ]
)

markup_add_homework = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Быстро добавить", callback_data="fast_add")],
        [InlineKeyboardButton(text="Добавить на дату", callback_data="on_date_add")],
        [InlineKeyboardButton(text="Меню", callback_data="menu")],
    ]
)


def get_markup_student_menu(is_admin) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Добавить дз📌", callback_data="add_homework"),
                InlineKeyboardButton(text="Получить дз🔍", callback_data="get_homework"),
            ],
            [InlineKeyboardButton(text="Профиль👤", callback_data="profile")],
        ]
    )
    if is_admin:
        keyboard.add(InlineKeyboardButton(text="Класс⭐️", callback_data="class_menu"))

    return keyboard


markup_check_homework = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Да, все верно", callback_data=CheckHomework.new(boolean="true")
            )
        ],
        [
            InlineKeyboardButton(
                text="Нет", callback_data=CheckHomework.new(boolean="false")
            )
        ],
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
        [InlineKeyboardButton(text="Отмена", callback_data="false")],
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
    inline_keyboard=[
        [InlineKeyboardButton(text="Вернуться в меню", callback_data="menu")]
    ]
)


markup_class_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Добавить администратора", callback_data="add_admin"
            )
        ],
        [InlineKeyboardButton(text="Сменить токен", callback_data="remove_token")],
        [InlineKeyboardButton(text="Кикнуть одноклассника", callback_data="kick")],
        [InlineKeyboardButton(text="Меню", callback_data="menu")],
    ]
)


def get_markup_classmates(data):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for key in data.keys():
        keyboard.insert(
            InlineKeyboardButton(text=data[key], callback_data=StudentsData.new(key))
        )
    keyboard.add(InlineKeyboardButton(text="Меню", callback_data="menu"))
    return keyboard


# | Developer | Developer | Developer | Developer | Developer | Developer | Developer | Developer |


markup_developer_menu = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Рассылка", callback_data="mailing")]]
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
