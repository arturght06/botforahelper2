from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


button_type_all = KeyboardButton('Все')
button_type_some = KeyboardButton('Некоторые')
button_cancel = KeyboardButton('Отмена')

settings_key = ReplyKeyboardMarkup(resize_keyboard=True).row(button_type_all, button_type_some).add(button_cancel)

brcs_key = ReplyKeyboardMarkup(resize_keyboard=True).add(button_cancel)

button_num = KeyboardButton('Номера')
button_add_num = KeyboardButton('Добавить номер')
button_del_num = KeyboardButton("Удалить номер") 

button_bar = KeyboardButton('Штрих-код')
button_create = KeyboardButton('Создать штрих-код')

greet_key = ReplyKeyboardMarkup(resize_keyboard=True).row(button_num, button_add_num, button_del_num).row(button_bar, button_create)

