import asyncio
import logging
from aiogram import Dispatcher, Bot
from config import Config, load_config
from handlers import user_handlers, some_handlers, test_handlers
from keyboards.main_menu_bar import create_menu_keyboard

logger = logging.getLogger(__name__) #-> инициализирум логгер

async def main(): #--> главаня функция бота
    
    #создаем логгер и выводим информацию в консоль
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                        '[%(asctime)s] - %(name)s - %(message)s')
    #сообщение о начале работы бота
    logger.info('Starting bot')
    
    #инициализация конфигурации
    config: Config = load_config()
    
    #объект бота
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    
    #инициализирум диспечер
    dp: Dispatcher = Dispatcher()
    
    await create_menu_keyboard(bot)

    #подлючаем роутеры в порядке переоритета
    dp.include_router(user_handlers.router)
    # dp.include_router(test_handlers.router)
    dp.include_router(some_handlers.router)
    
    #удаляем все сообщщения которые могли придти пока бот не активен
    await bot.delete_webhook(drop_pending_updates=True)
    
    #запуск бота
    await dp.start_polling(bot)    
    
if __name__ == '__main__':
    asyncio.run(main())