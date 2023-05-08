from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_wheather import LEXICON_WH
#клавиатура для любимых городов
def create_keyboard(*args: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    
    for button in args:
        kb_builder.row(InlineKeyboardButton(
            text=button,
            callback_data=f"погода {str(button)}"))
        
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON_WH['edit_city'],
        callback_data='edit_city'),
        InlineKeyboardButton(
            text=LEXICON_WH['cancel'],
            callback_data='cancel'),
        width=2
        )
    return kb_builder.as_markup()
#клавиатура для удаления городов из списка пользователя
#callback для удаления ИМЯisdel
def create_edit_keyboard(*args: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    
    for button in args:
        kb_builder.row(InlineKeyboardButton(
            text=f"{LEXICON_WH['del']} - {button}",
            callback_data=f"{button}isdel"))
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON_WH['cancel'],
        callback_data='cancel'))
    return kb_builder.as_markup()