from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from services.restapi.restapi import is_student


class StudentFilter(BoundFilter):
    async def check(self, msg: types.Message or types.CallbackQuery):
        tguser_id = msg.from_user.id
        if isinstance(msg, types.CallbackQuery):
            msg = msg.message
        return msg.chat["type"] == "private" and await is_student(tguser_id)