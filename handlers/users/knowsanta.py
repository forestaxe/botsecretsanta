from aiogram import types
from loader import dp, db, bot
from aiogram.dispatcher.filters.state import StatesGroup, State


class namewish(StatesGroup):
   user = State()
   name = State()
   wish = State()


@dp.callback_query_handler(lambda callback_query: callback_query.data == "button2")
async def whoismysanta(callback_query: types.CallbackQuery):

    list = []
    b = await db.read_all_enduser()
    x = len(b)

    for i in range (x):
        list.append(await db.read_enduser(i))

    if not list:
        print(123123123)
        await bot.send_message(chat_id=callback_query.from_user.id, text="Упс... Кажется жеребьёвка ещё не завершена, мы вас оповестим!)")

    for i in range(len(list)):
        z = list[i]
        print('z', z)
        if callback_query.from_user.id == z:
            if i+1 == len(list):
                kid = list[0]
            else:
                kid = list[i+1]

    wish = await db.read_wish_data(kid)
    name = await db.read_name_data(kid)

    await bot.send_message(chat_id=callback_query.from_user.id, text=f"Поздравляю! Тебе достался(-ась) {name}🎄 \n \n"
    f"Теперь ты должен сделать этому человеку что-то приятное :) Лайк поставь, напиши что-то приятное... "
    f"\nНе хочешь- не придумывай, мне то что)\n\n"
    f"Если решишь быть хорошим другом, вот чего хочет твой человечек) 🎁 \n\n"
    f"Wish list {name}: \n"
    f"{wish}")

