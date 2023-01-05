from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from random import choice

from dispatcher import dp, bot
from database import dbase
from keyboards.general_kb import kb_general


HELP_TEXT = '''
<b>/help</b> - <em>список доступных комманд;</em>
<b>/stats</b> - <em>вывод статистики;</em>
<b>/zadan</b> - <em>вывод заданий;</em>'''

ZADANS = ['https://kpolyakov.spb.ru/cms/images/5875.gif',
          'https://kpolyakov.spb.ru/cms/images/5874.gif',
          'https://kpolyakov.spb.ru/cms/images/5873.gif',
          'https://kpolyakov.spb.ru/cms/images/5436.gif',
          'https://kpolyakov.spb.ru/cms/images/74.gif']


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text="Привет! Это бот для подготовки к ЕГЭ.\nСписок доступных комманд - /help",
                         reply_markup=kb_general)
    await message.delete()
    await dbase.sql_regis(message.chat.id)


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_TEXT,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['stats'])
async def cmd_stats(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вот ваша статистика')
    await message.delete()


@dp.message_handler(commands=['zadan'])
async def cmd_zadan(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=choice(ZADANS))
    await message.delete()


@dp.message_handler(Text(equals='Задания'),
                    content_types=['text'])
async def text_zadan(message: types.Message):
    # await message.answer_document(document=)
    await message.delete()


@dp.message_handler(Text(equals='Статистика'),
                    content_types=['text'])
async def text_stats(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вот ваша статистика')
    await message.delete()


def reg_handlers_general(dpr: Dispatcher):
    dpr.register_message_handler(cmd_start,
                                 commands=['start'])
    dpr.register_message_handler(cmd_help,
                                 commands=['help'])
    dpr.register_message_handler(cmd_stats,
                                 commands=['stats'])
    dpr.register_message_handler(cmd_zadan,
                                 commands=['zadan'])
    dpr.register_message_handler(text_zadan,
                                 content_types=['text'])
    dpr.register_message_handler(text_stats,
                                 content_types=['text'])
