from aiogram import types, bot
from loader import dp

@dp.message_handler(commands=["send"])
async def sendmessage(message: types.Message):
    # Отправка сообщения конкретному пользователю
    await dp.bot.send_message(chat_id={message.chat.id}, text="Вы указали в поле пожеланий к подарку - "
                                                       "*Шариковая ручка, сертификат в ювелирный магазин* "
                                                       "Пожалуйста, зайдите в бота и, если не видите кнопки"
                                                       "*Принять участие* и *Чей я Санта?* - продублируйте команду "
                                                       "/start \n"
                                                       "Нажмите на кнопку *Принять участие* и введите в первом сообщении"
                                                       " свои имя и фамилию, а во втором укажите пожелания к подарку. :)\n"
                                                       "Вы сможете узнать чей вы Санта после проведения жеребьёвки."
                                                      " Мы вас оповестим!" )
