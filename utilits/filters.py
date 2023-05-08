from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message
from lexicon.lexicon import valut_symbol

class CheckIsCheckValutMsg(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        text = message.text
        #checking msg is what valut
        return text in valut_symbol