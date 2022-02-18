from keyboard import greet_key
from aiogram import Dispatcher
from create_bot import dp
from database import sqlitedb


# @dp.message_handler(commands=['start'])
async def process_hi_command(message):
    await message.answer_sticker(r'CAACAgQAAxkBAAEDy5Fh-x-svmcxY5AZKtmbD1ey64QiwAACiAADLOlYDEVV-cLQgV_2IwQ')
    await message.reply(f'{str(message.from_user.id)}\nПривет22👋🏽\nЭтот бот проверяет информацию об аккаунте в приложении \"Fora\"ПСС...  кнопка уже внизу👇' , reply_markup=greet_key)

# async def echo(message):
#     a = await sqlitedb.sql_add_number(message.from_user.id, message.text)
#     if a == False:
#         await bot.send_message(chat_id=message.from_user.id, text='axcs token is wrong')
#     else:
#         a(message.from_user.id, message.text)

# async def echo(message):
#     a = await sqlitedb.sql_all_numbers(message.from_user.id)
#     if len(a) == 0:
#         await message.reply(text='You doesn`t have some numbers')
#     else:
#         await message.reply(text=str(a) + 'not none')

def register_handlers_settings(dp: Dispatcher):
    dp.register_message_handler(process_hi_command, text = ['Отмена', '/start'])
    # dp.register_message_handler(echo)
