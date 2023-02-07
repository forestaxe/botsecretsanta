from aiogram import types
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards.default.santabuttons import changekeyboard

class FSMInputName(StatesGroup):
   wish = State()
   change = State()

@dp.callback_query_handler(lambda callback_query: callback_query.data == "button1" )
async def process_callback_button1(callback_query: types.CallbackQuery):
   ids = []
   ids2= []
   b = await db.user_data()
   x = len(b)
   print(x)

   for i in range(x):
      ids.append(await db.get_all_id(i))
      ids2.append(await db.read_id_data(i))
   print(ids, ids2)



   user_id = callback_query.from_user.id
   print(user_id)

   if user_id in ids and not user_id in ids2:
      await bot.send_message(chat_id=callback_query.from_user.id, text="Напишите свои пожелания к подарку")
      await FSMInputName.wish.set()
   elif user_id not in ids:
      await db.get_user_id(user_id)
      await bot.send_message(chat_id=callback_query.from_user.id, text="Напишите свои пожелания к подарку")
      await FSMInputName.wish.set()
   elif user_id in ids and user_id in ids2:
      wishes = await db.read_wish_data(callback_query.from_user.id)
      await bot.send_message(chat_id=callback_query.from_user.id, text=f'Вы уже ввели пожелания, хотите их изменить? \nВаши пожелания: {wishes}' , reply_markup=changekeyboard)


#
#
# @dp.message_handler(text="Принять участие")
# async def user_reg(message: types.Message):
#    ids = []
#    b = await db.user_data()
#    x = len(b)
#    print(x)
#
#    for i in range(x):
#        ids.append(await db.get_all_id(i))
#    print(ids)
#
#    user_id = message.from_user.id
#
#    if user_id in ids:
#       await message.answer("Напишите, пожалуйста, Ваши пожелания к подарку!")
#       await FSMInputName.wish.set()
#    else:
#       await db.get_user_id(user_id)
#       await message.answer("Напишите, пожалуйста, Ваши пожелания к подарку!")
#       await FSMInputName.wish.set()

@dp.message_handler(state=FSMInputName.wish)
async def state_name(message: types.Message, state: FSMContext):
   async with state.proxy() as data:
      data['wish'] = message.text
      print(data['wish'])

      user_id = message.from_user.id
      user_name = message.from_user.full_name
      user_wish = data['wish']
      print('123')

      try:
         await db.insert_data(user_id, user_name, user_wish)
         await message.answer("Пожелания успешно добавлены")
      except:
         OSError
      await state.finish()


@dp.callback_query_handler(lambda callback_query: callback_query.data == "button3")
async def changewish(callback: types.CallbackQuery):
   await callback.message.answer('Введите новые пожелания')
   await FSMInputName.change.set()

@dp.message_handler(state=FSMInputName.change)
async def state_name(message: types.Message, state: FSMContext):
   async with state.proxy() as data:
      await FSMInputName.change.set()
      data['change'] = message.text
      print(data['change'])

      oldstring = await db.read_wish_data(message.chat.id)
      newstring = data['change']

      try:
         await db.change_data(oldstring, newstring)
         await message.answer("Успешно изменены")
      except:
         OSError

      await state.finish()
#
# #Регистрация пользователей
#
# @dp.message_handler(text="Принять участие")
# async def cmd_tese1(message: types.Message):
#    file = open("data.txt", "r")
#    users = set()
#    for line in file:
#       users.add(line.strip())
#
#    if not str(message.chat.id) in users:
#       await message.answer("Напишите, пожалуйста, Ваше имя и фамилию")
#       await FSMInputName.name.set()
#    else:
#       await message.answer("Вы уже участвуете!")
#
# @dp.message_handler(state=FSMInputName.name)
# async def state1(message: types.Message, state: FSMContext):
#    async with state.proxy() as data:
#       data['name'] = message.text
#       print(data)
#    # await message.answer(data['name'])
#    await message.answer("Напишите, пожалуйста, Ваш список желаний (wish list) \n *В одну строчку, через запятую*")
#    await FSMInputName.next()
#
#    @dp.message_handler(state=FSMInputName.wish)
#    async def state2(message: types.Message, state: FSMContext):
#       async with state.proxy() as data:
#          data['wish'] = message.text
#          print(data)
#       # await message.answer(data['wish'])
#       file = open("data.txt", "a")
#       file.write(str(message.chat.id) + "\n")
#       file.write(str(data['name']) + "\n")
#       file.write(str(data['wish']) + "\n")
#       await state.finish()
#       await message.answer("Спасибо, мы зарегистрировали Вас в качестве участника. "
#                            "Как будет проведена жеребьевка, Вы сможете узнать, "
#                            "кому дарите подарок, нажав кнопку *Чей я Санта*")
#    # после этого данные в fsm пропадают, поэтому думайте когда закрывать стейт

