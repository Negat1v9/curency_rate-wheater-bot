from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import valut_symbol

def create_keyboard_valut()->ReplyKeyboardMarkup:
    bottons = []
    keybord = []
    for i in range(len(valut_symbol)):
        bottons.append(KeyboardButton(text=valut_symbol[i]))
        if len(bottons) == 4:
            keybord.append(bottons)
            bottons = []
        
    user_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=keybord,)
    return user_kb