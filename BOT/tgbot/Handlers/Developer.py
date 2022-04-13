from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from bot import dp
from tgbot.Filters.DeveloperFilter import DeveloperFilter

# Tasks:
# 1) Создание рассылок


@dp.message_handler(DeveloperFilter(), commands=["dev_panel"], state="*")
async def dev_panel(msg: Message):
    await msg.answer("Developer panel")