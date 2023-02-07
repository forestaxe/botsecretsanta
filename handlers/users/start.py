from aiogram import types
from loader import bot
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
    print(message.from_user.id)
    await message.answer("Добрый день! Если хочешь поучаствовать в игре «Тайный Санта» 🎅 и "
                         "тем самым порадовать своих друзей, 🌟 то нажми на кнопку 'Принять участие'",
                         reply_markup=santakeyboard)


    # await callback_query.answer('123')
    # await bot.send_message()

    # ids = []
    # b = await db.user_data()
    # x = len(b)
    # print(x)
    # for i in range(x):
    #     ids.append(await db.get_all_id(i))
    #     # await db
    # print(ids)
    # await message.answer(f"Your user_id: {ids}")

