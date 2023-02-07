from aiogram import types
from loader import dp, db, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

class namewish(StatesGroup):
   user = State()
   name = State()
   wish = State()

@dp.callback_query_handler(lambda callback_query: callback_query.data == "button2")
async def whoismysanta(callback_query: types.CallbackQuery):

    # Сообщение выводится до проведения жеребьёвки.
    # await message.answer("Жеребьёвка ещё не проведена, мы вас оповестим :)")

    list = []
    b = await db.read_all_enduser()
    x = len(b)
    print(x)

    for i in range (x):
        list.append(await db.read_enduser(i))

    print(list)

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
    print(kid)

    wish = await db.read_wish_data(kid)
    print(wish)
    name = await db.read_name_data(kid)

    await bot.send_message(chat_id=callback_query.from_user.id, text=f"Поздравляю! Тебе достался(-ась) {name}🎄 \n \n"
    f"Теперь ты должен сделать этому человеку что-то приятное :) Лайк поставь, напиши что-то приятное... "
    f"\nНе хочешь- не придумывай, мне то что)\n\n"
    f"Если решишь быть хорошим другом, вот чего хочет твой человечек) 🎁 \n\n"
    f"Wish list {name}: \n"
    f"{wish}")
    #
    # userdata = []
    # list1 =[]
    # file = open("data.txt", "r")
    # datanum = 0
    # urnum = 0
    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     try:
    #         letter=int(line.strip())
    #     except:
    #         OSError
    #         pass
    #
    #     if kid != letter:
    #         datanum += 1
    #     else:
    #         urnum = datanum
    #
    #     userdata.append(line)
    #
    #     list1.append(line.strip())
    #
    #
    # await message.answer(f"Поздравляем! Вы будете Тайным Сантой для {list1[urnum+1]}🎄 \n \n"
    #                      f"Просим учесть, что подарок должен соответствовать гастрономической тематике нашего мероприятия, "
    #                      f"а также быть номиналом до 10 000 ₽. \n\n"
    #                      f"Направляем wish list Вашего кандидата для ориентира при выборе подарка 🎁 \n\n"
    #                      f"Wish list {list1[urnum+1]}: \n"
    #                      f"{list1[urnum+2]}")

