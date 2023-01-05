from colorama import Fore
from aiogram import executor

from database import dbase
from dispatcher import bot, dp
from handlers.general import reg_handlers_general


async def startup(_):
    print(Fore.GREEN + 'The bot went online!')
    dbase.sql_start()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=startup)
    reg_handlers_general(dpr=dp)
