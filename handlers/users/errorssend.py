from aiogram import types, bot
from loader import dp



@dp.message_handler(commands=["error"])
async def senderrors(message:types.Message):

 # Рассылка уведомлений о не введенных Имени и Пожеланиях

    datauser = open("data.txt", "r")
    datalist = []
    userlist= []
    sendlist = []
    while True:
        line = datauser.readline()
        if not line:
            break
        try:
            letter=int(line.strip())
            datalist.append(letter)
        except:
            OSError
            pass

    users = open("user.txt", "r")
    while True:
        line1 = users.readline()
        if not line1:
            break
        letter1=int(line1.strip())
        userlist.append(letter1)

    for i in range (len(userlist)):
        c = 0
        for j in range (len(datalist)):
            if datalist[j] == userlist[i]:
                break
            else:
                c+=1
            if c == len(datalist):
                sendlist.append(userlist[i])

    sendlist.append(294349333)

    for z in range (len(sendlist)):
        await dp.bot.send_message(chat_id=sendlist[z], text="Вы не указали свои желания, пожалуйста, продублируйте команду"
                                                            " /start и нажмите на кнопку"
                                             "*Принять участие*, введите в первом сообщении имя, а во "
                                             "втором - список пожеланий к подарку :)")