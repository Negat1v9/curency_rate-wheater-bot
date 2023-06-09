from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_curency import valut_symbol, LEXICON

def create_keyboard_valut()->ReplyKeyboardMarkup:
    bottons = []
    keybord = []
    for i in range(len(valut_symbol)):
        bottons.append(KeyboardButton(text=valut_symbol[i]))
        if len(bottons) == 4:
            keybord.append(bottons)
            bottons = []
    keybord.append([KeyboardButton(text=LEXICON['all_valut'])])
        
    user_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=keybord)
    return user_kb