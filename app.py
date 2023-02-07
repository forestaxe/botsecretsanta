from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

from loader import db

from utils.db_api.postgresql import Database

async def on_startup(dp):
    await set_default_commands(dp)
    await on_startup_notify(dp)
    await db.create()
    print (await db.user_data())

if __name__ == '__main__':

    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
