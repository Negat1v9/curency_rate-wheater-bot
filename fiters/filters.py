from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon_curency import valut_symbol, LEXICON
#редакторование городов
class IsEditListCyty(BaseFilter):
    async def __call__(self, call_back: CallbackQuery):
        return isinstance(call_back.data, str) and 'isdel' in call_back.data
    
class WheatherMessage(BaseFilter):
    async def __call__(self, message: Message):
        msg: list = message.text.strip().split()
        return 'погода' in msg[0].lower() and isinstance(msg[-1], str)\
            and len(msg) >= 2
            
class WheaterCallBack(BaseFilter):
    async def __call__(self, call_back: CallbackQuery) -> bool:
        data: str = call_back.data
        return 'погода' in data
    
class AddUsersCity(BaseFilter):
    async def __call__(self, message: Message):
        msg: list = message.text.strip().split()
        return 'добавить' in msg[0].lower() and len(msg) >= 2
    
class CheckIsCheckValutMsg(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        text = message.text
        #checking msg is what valut
        return text in valut_symbol
    
class CheckIsAllValut(BaseFilter):
    async def __call__(self, message: Message):
        return message.text == LEXICON['all_valut']