from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_btn_1 = InlineKeyboardButton('Принять участие', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Чей я Санта?', callback_data='button2')
inline_btn_3 = InlineKeyboardButton('Изменить', callback_data='button3')


santakeyboard = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)

changekeyboard= InlineKeyboardMarkup().add(inline_btn_3)