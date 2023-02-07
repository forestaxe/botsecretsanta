from aiogram import types
from aiogram.dispatcher.dispatcher import Command
from keyboards.default.santabuttons import santakeyboard

from loader import dp, db


@dp.message_handler(Command("start"))
async def command_start(message: types.Message):

    a = message.from_user.id

    try:
        await db.get_user_id(a)

    except:
        OSError

    await message.answer("Добрый день! Если хочешь поучаствовать в игре «Тайный Санта» 🎅 и "
                         "тем самым порадовать своих друзей, 🌟 то нажми на кнопку 'Принять участие'",
                         reply_markup=santakeyboard)