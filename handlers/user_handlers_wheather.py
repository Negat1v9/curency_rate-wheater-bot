from aiogram import Router
from aiogram.filters import (CommandStart, Command, Text)
from aiogram.types import (Message, CallbackQuery, ReplyKeyboardRemove)
from wheather.wheather_get import (get_wheather, parse_msg)
from lexicon.lexicon_wheather import LEXICON_WH
from keyboards.keybord_wheather import (create_keyboard, create_edit_keyboard)
from fiters.filters import (IsEditListCyty, WheatherMessage, \
    WheaterCallBack, AddUsersCity)
# from database.db_users import User#change this
from user.class_user import User


router: Router = Router()

@router.message(WheatherMessage())
async def process_wheather_message(message: Message):
    data = parse_msg(message.text)
    wheather = get_wheather(data)
    if wheather['message']:
        await message.answer(
            text=wheather['message'],
            reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(
            text=wheather['error'],
            reply_markup=ReplyKeyboardRemove())
    
@router.message(Command(commands='favorite'))
async def process_add_favorite(message: Message):
    userid = int(message.from_user.id)
    user = User(userid=userid)
    citys: list = user.get_user_city()
    if citys:
        await message.answer(
            text=LEXICON_WH['/favorite'],
            reply_markup=create_keyboard(
                *citys))
    else:
        await message.answer(
            text=LEXICON_WH['not_user_city'])

@router.message(AddUsersCity())
async def process_add_city_command(message: Message):
    data = parse_msg(message.text)
    userid = int(message.from_user.id)
    user = User(userid=userid)
    citys: list = user.get_user_city()
    if data not in citys:
        status = get_wheather(data)
        if status['status_code'] == 200:
            await message.answer(
                text=LEXICON_WH['add_city'])
            user.add_user_city(data)
        else:
            await message.answer(
                text=LEXICON_WH['error_msg'])
    else:
        await message.answer(
            text=LEXICON_WH['already_theare'])
        
@router.callback_query(WheaterCallBack())
async def process_wheather_callback(callback: CallbackQuery):
    data = parse_msg(callback.data)
    wheather = get_wheather(data)
    if wheather['message']:
        await callback.message.answer(
            text=wheather['message'])
    else:
        await callback.message.answer(
            text=LEXICON_WH['error_server'])
        
@router.callback_query(Text(text='edit_city'))
async def process_redaction_city(callback: CallbackQuery):
    userid = int(callback.from_user.id)
    user = User(userid=userid)
    citys: list = user.get_user_city()
    await callback.message.edit_text(
        text=LEXICON_WH['edit_city'],
        reply_markup=create_edit_keyboard(
            *citys))
    
@router.callback_query(IsEditListCyty())
async def process_delete_city(callback: CallbackQuery):
    delcity: str = str(callback.data).replace('isdel', '')
    userid = int(callback.from_user.id)
    user = User(userid=userid)
    citys: list = user.get_user_city()
    citys.remove(delcity)
    if citys:
        await callback.message.edit_text(
            text=LEXICON_WH['edit_city'],
            reply_markup=create_edit_keyboard(
                *citys))
    else:
        await callback.message.edit_text(
            text=LEXICON_WH['nothing_in_db'])
    user.del_user_city(citys)
        
@router.callback_query(Text(text='cancel'))
async def process_cancel_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_WH['cancel_press'])
    