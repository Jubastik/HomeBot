from aiogram.types import CallbackQuery, Message, User
from asyncio import sleep

from tgbot.entities.stage import Stage
from languages.text_keys import TextKeys
from languages.text_proccesor import process_text
from tgbot.keyboards.inline.markup import markup_start

from bot import bot


class EntryStage(Stage):
    name = "entry_stage"

    def __init__(self, mode) -> None:
        super().__init__(mode)
        self.markup = markup_start

    async def activate(self, status: str = ""):
        if self.user.main_msg_id is None:
            main_msg_id = await bot.send_message(
                chat_id=self.user.tgid,
                text=process_text(TextKeys.hello, status=status),
                reply_markup=self.markup,
            )
            return main_msg_id.message_id
        else:
            await bot.edit_message_text(
                chat_id=self.user.userid,
                message_id=self.user.main_msg_id,
                text=process_text(TextKeys.hello, status=status),
                reply_markup=self.markup,
            )
            return self.user.main_msg_id