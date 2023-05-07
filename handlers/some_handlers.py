from aiogram import Router
from aiogram.types import Message

router: Router = Router()

@router.message()
async def process_some_message(message: Message):
    await message.answer(text="Увы, но я пока что не знаю такую команду")