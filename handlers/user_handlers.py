from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import LEXICON
from keyboards.keyboards import create_keyboard_valut
from database.class_database import DataBase
from user.class_user import User


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