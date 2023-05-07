from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import LEXICON
from keyboards.keyboards import create_keyboard_valut
from database.class_database import DataBase


router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'])
    
    
@router.message(Command(['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['help'])