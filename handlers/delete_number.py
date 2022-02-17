from keyboard import greet_key, brcs_key
from aiogram import Dispatcher, types
from create_bot import dp, bot
from database import sqlitedb
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from reqdata import req
from database import sqlitedb

class FSMdelnum(StatesGroup):
    that = State()


# @dp.message_handler(commands=['start'])
async def start_del_number(message):
    await FSMdelnum.that.set()
    all_numbers = await sqlitedb.sql_find_all_numbers(str(message.from_user.id))
    if len(all_numbers) == 0:
        await bot.send_message(chat_id=message.from_user.id, text='У тебя нет номеров ', reply_markup=brcs_key)
        return
    else:
        string_out = 'Выбери номер:\n'
        for t in range(len(all_numbers)):
            string_out += f"{t}. <b>{str(all_numbers[t][0])}</b>\n"
        print(string_out)

        await message.reply(text=string_out, reply_markup=brcs_key)


async def deler(message):
    aid = str(message.text)
    userid = str(message.from_user.id)
    # info_number = req(acstkn)
    all_numbbers = await sqlitedb.sql_find_all_numbers(str(message.from_user.id))
    # 
    try:
        
        number_for_delete = str(all_numbbers[int(aid)][0])

        print(await sqlitedb.delete_number(userid, number_for_delete))
        await bot.send_message(message.from_user.id, text=f'Номер - {number_for_delete} - удален')
    except:
        message.reply('Невозможно удалить')

    # if info_number == False:
    #     await message.reply(req(acstkn))
    # else:
        



async def back(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(chat_id = message.from_user.id, text = 'Ok', reply_markup=greet_key)


def register_handlers_del_numbers(dp: Dispatcher):
    dp.register_message_handler(back, state='*', commands=['Отмена', 'back'])
    dp.register_message_handler(back, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(start_del_number, text = ["Удалить номер"], state=None)
    dp.register_message_handler(deler, state=FSMdelnum.that)