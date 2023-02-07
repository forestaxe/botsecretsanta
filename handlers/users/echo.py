from aiogram import types
from loader import dp
from keyboards.default.santabuttons import santakeyboard
# from keyboards.default.mainmenu import menu

@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')


