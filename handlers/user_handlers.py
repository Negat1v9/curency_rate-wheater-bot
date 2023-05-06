from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import LEXICON
from keyboards.keyboards import create_keyboard_valut


router: Router = Router()

