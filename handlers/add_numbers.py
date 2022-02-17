from keyboard import greet_key, brcs_key
from aiogram import Dispatcher, types
from create_bot import dp, bot
from database import sqlitedb
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from reqdata import req
from database import sqlitedb

class FSMaddnum(StatesGroup):
    that = State()


# @dp.message_handler(commands=['start'])
async def start_add_number(message):
    await FSMaddnum.that.set()
    with open('settings.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await bot.send_message(chat_id=message.from_user.id, text='Что-бы добавить - номер отправь access-token\nВзять его можно так:\nЗайди в аккаунт Форы в Chrome, нажми правой кнопкой миши -> просмотреть код -> открой вкладку Network -> перезагрузи страницу -> просмотри любой запрос справа и наконец скопируй значение переменной access-token, как на фото', reply_markup=brcs_key)
    # await message.reply(f'{str(message.from_user.id)}\nПривет👋🏽\nЭтот бот проверяет информацию об аккаунте в приложении \"Fora\"ПСС...  кнопка уже внизу👇' , reply_markup=greet_key)


async def add_number_in_db(message):
    acstkn = str(message.text)
    userid = str(message.from_user.id)
    # info_number = req(acstkn)

    a = await sqlitedb.sql_add_number(userid, acstkn)
    print(str(a))
    if a == 'FalseNumber' or a == False:
        await message.reply('Такой номер уже добавлен или токен устарел')
        return
    else:
        await message.reply('Номер успешно добавлен')
        return

    # if info_number == False:
    #     await message.reply(req(acstkn))
    # else:
        



async def back(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(chat_id = message.from_user.id, text = 'Ok', reply_markup=greet_key)


def register_handlers_add_numbers(dp: Dispatcher):
    dp.register_message_handler(back, state='*', commands=['Отмена', 'back'])
    dp.register_message_handler(back, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(start_add_number, text = ['Добавить номер'])
    dp.register_message_handler(add_number_in_db, state=FSMaddnum.that)

    # dp.register_message_handler(echo)