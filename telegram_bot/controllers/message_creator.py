from aiogram.types import InlineKeyboardMarkup, Message, ParseMode;
from collections import namedtuple
MessageArgs = namedtuple('MessageArgs', 'text parse_mode reply_markup')
class MessageCreator:
    def __init__(self, content: str, reply_markup: InlineKeyboardMarkup | None = None, parse_mode: str | None = ParseMode.HTML) -> None:
        self.contet = content
        self.reply_markup = reply_markup
        self.parse_mode = parse_mode
    def get_args(self) -> MessageArgs:
        return {'text': self.contet, 'parse_mode': self.parse_mode, 'reply_markup': self.reply_markup}

    def format(self, *args):
        return MessageCreator(self.contet.format(*args), self.reply_markup, self.parse_mode)
        
    async def edit_to(self, message: Message) -> None:
        await message.edit_text(self.contet, parse_mode=self.parse_mode)
        await message.edit_reply_markup(self.reply_markup)
