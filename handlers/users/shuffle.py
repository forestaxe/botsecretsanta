from aiogram import types
from loader import dp,db, bot
import random


#Перемешка пользователей
@dp.message_handler(commands=["shuffle"])
async def shuffle(message: types.Message):

    list = []
    b = await db.user_data()
    x = len(b)
    print(x)

    for i in range(x):
        list.append(await db.get_all_id(i))
    print(list)

    random.shuffle(list)
    print(list)

    await db.delete_enduser()

    for i in range(x):
        id = list[i]
        await bot.send_message(chat_id=id, text="Жеребьёвка завершена!")
        await db.write_enduser(id)

