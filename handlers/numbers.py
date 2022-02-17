from create_bot import bot, dp
from keyboard import settings_key, greet_key, brcs_key
from balance import all_0, all_1, all_the_number, all_numbers
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from balance import files
from config import pswrds
from database import sqlitedb
from reqdata import req

class FSMnumbers(StatesGroup):
    that = State()
    back = State()
    some_nums = State()

    

# @dp.message_handler(text=["Штрих-коды"], state = None)
async def cmd_start(message: types.Message):
    # Проверка, есть ли у пользователя номера или нет
    all_numbers = await sqlitedb.sql_find_all_numbers(str(message.from_user.id))

    if len(all_numbers) == 0:
        await bot.send_message(chat_id=message.from_user.id, text='У тебя нет номеров ' + str(message.from_user.id) + str(all_numbers), reply_markup=brcs_key)
    else:
        await bot.send_message(chat_id=message.from_user.id, text='Какие номера проверять', reply_markup=settings_key)
        await FSMnumbers.that.set()
    return





async def all_num(message: types.Message, state: FSMContext):
    all_numbers = await sqlitedb.sql_find_all_numbers(str(message.from_user.id))

    for i in all_numbers:
        text = await sqlitedb.sql_find_acstkn(i)
        response_info = req(text[0][0])
        print(response_info)
        if response_info == 'Ключ устарел':
            await bot.send_message(message.from_user.id, text=f'{i[0]} - {response_info}')
        else:
            a = 'Телефон: {0} \nБаланс: {1} \nБаллы: {2} \nКод штрих-кода: {3}'.format(response_info['phone_number'], response_info['currentbonus'], response_info['currentbalance'], response_info['barcode'])
            await bot.send_message(message.from_user.id, text=f'{a}')
    return
        # await bot.send_message()







# @dp.message_handler(content_types = ['text'], state = FSMbarcodes.that)
async def some_num(message: types.Message, state: FSMContext):
    all_numbers = await sqlitedb.sql_find_all_numbers(str(message.from_user.id))

    string_out = 'Выбери номер:\n'
    for t in range(len(all_numbers)):
        string_out += f"{t}. <b>{str(all_numbers[t][0])}</b>\n"
    
    await FSMnumbers.some_nums.set()

    print(string_out)
    await message.reply(text=string_out, reply_markup=brcs_key)







async def print_nums(message):
    print('message: ', message['text'])

    if message.text.replace(" ", "").isdigit() and len(message.text.split()) < 100:
        all_indexs = map(int, message.text.split())
    else:
        await bot.send_message(message.from_user.id, text='Неверный номер!')
        return

    # Поиск номеров по дб с этим пользователем
    all_numbers = await sqlitedb.sql_find_all_numbers(str(message.from_user.id))

    arr_numbers_info = []
    for index_num in all_indexs:
        try:
            x = all_numbers[index_num]
        except:
            await bot.send_message(message.from_user.id, text='Неверный номер')
            return
        # print(x, index_num)
        barc = await sqlitedb.sql_find_acstkn(x)
        barc = barc[0][0]

        info = req(barc)
        if info == 'Ключ устарел':
            await bot.send_message(message.from_user.id, text=f'{x[0]} - {info}')
            return
        else:
            a = 'Телефон: {0} \nБаланс: {1} \nБаллы: {2} \nКод штрих-кода: {3}'.format(info['phone_number'], info['currentbonus'], info['currentbalance'], info['barcode'])
            await bot.send_message(message.from_user.id, text=f'{a}')
        arr_numbers_info.append(info)

    print(arr_numbers_info)









async def back(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(chat_id = message.from_user.id, text = 'Ok', reply_markup=greet_key)

def register_handlers_numbers(dp: Dispatcher):
    dp.register_message_handler(back, state='*', commands=['Отмена', 'back'])
    dp.register_message_handler(back, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(cmd_start, text=["Номера"], state=None)
    dp.register_message_handler(some_num, text=["Некоторые"], state = FSMnumbers.that)
    dp.register_message_handler(all_num, text=["Все"], state = FSMnumbers.that)
    dp.register_message_handler(print_nums, state = FSMnumbers.some_nums)

