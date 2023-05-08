from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon_curency import Bot_commands

async def create_menu_keyboard(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
        )for command, description in Bot_commands.items()]
    await bot.set_my_commands(main_menu_commands)