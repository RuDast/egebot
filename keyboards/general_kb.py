from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_general = ReplyKeyboardMarkup(resize_keyboard=True)

kb_general.add(KeyboardButton(text='Статистика'),
               KeyboardButton(text='Задания'))
