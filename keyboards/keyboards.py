from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# from lexicon.lexicon import

def create_keyboard_valut(*args)->ReplyKeyboardMarkup:
    
    keybord: list[list[KeyboardButton()]] = [
        [KeyboardButton(text=text)] for text in args]
    
    user_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=keybord, resize_keyboard=True)
    return user_kb