import asyncio
import logging
from aiogram import Dispatcher, Bot
from config import Config, load_config
from handlers import (some_handlers,
                    user_handlers_curency,
                    user_handlers_wheather,
                    test_handlers)
from keyboards.main_menu_bar import create_menu_keyboard

logger = logging.getLogger(__name__) #-> инициализирум логгер

async def main(): #--> main func 
    
    #create looger to write in terminal
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                        '[%(asctime)s] - %(name)s - %(message)s')
    #msg from logger about Bot is start
    logger.info('Starting bot')
    
    #load config for tg_token
    config: Config = load_config()
    
    #object bot
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    
    #Dispatcher
    dp: Dispatcher = Dispatcher()
    
    #bot creating menu-bar
    await create_menu_keyboard(bot)

    #router curency handelrs
    dp.include_router(user_handlers_curency.router)
    
    #router wheather handlers
    dp.include_router(user_handlers_wheather.router)
    
    #test handlers -> off
    # dp.include_router(test_handlers.router)
    
    #others handlers
    dp.include_router(some_handlers.router)
    
    #delete msg from time then bot was offline
    await bot.delete_webhook(drop_pending_updates=True)
    
    #start polling bot for updates
    await dp.start_polling(bot)    
    
if __name__ == '__main__':
    asyncio.run(main())