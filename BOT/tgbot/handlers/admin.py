from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from BOT.bot import dp
from BOT.tgbot.filters.admin_filter import AdminFilter

# Tasks:
# 1) Изменение/удаление домашки в классе


@dp.message_handler(AdminFilter(), commands=["admin_panel"], state="*")
async def admin_panel(msg: Message):
    await msg.answer("Админка")