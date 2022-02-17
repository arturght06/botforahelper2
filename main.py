from config import admin_id
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import keyboard
from create_bot import bot, dp
from database import sqlitedb

async def send_admin(dp):
    await bot.send_message(chat_id = admin_id, text = "Bot was started")
    print("Bot was started")
    sqlitedb.sql_start()

from handlers import barcodes, numbers, settings, create, add_numbers, delete_number

settings.register_handlers_settings(dp)
numbers.register_handlers_numbers(dp)
barcodes.register_handlers_barcodes(dp)
create.register_handlers_create(dp)
add_numbers.register_handlers_add_numbers(dp)
delete_number.register_handlers_del_numbers(dp)


executor.start_polling(dp, on_startup=send_admin, skip_updates=True)
