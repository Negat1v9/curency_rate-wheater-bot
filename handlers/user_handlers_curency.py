from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from lexicon.lexicon_curency import LEXICON
from fiters.filters import CheckIsCheckValutMsg
from keyboards.keyboards_curency import create_keyboard_valut
from curency.requests_curency import get_curency
from user.class_user import User
from msg_parse.parsing import get_done_msg


router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'])
    
    userid = int(message.from_user.id)
    user: User = User(userid=userid)
    user.init_user()
    
    
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])
    
@router.message(Command(commands='commands'))
async def process_show_commands(message: Message):
    await message.answer(text=LEXICON['/commands'])
    
@router.message(Command(commands='curency'))
async def process_kb_curency(message: Message):
    await message.answer(text=LEXICON['curency'],
        reply_markup=create_keyboard_valut())
    
@router.message(CheckIsCheckValutMsg())
async def process_valut_checking(message: Message):
    curency: dict = get_curency()
    curency_text = get_done_msg(curency=curency,
                                 message=message.text)
    await message.answer(text=curency_text)
    