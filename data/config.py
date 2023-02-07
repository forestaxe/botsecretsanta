import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))


admins = [

]

dbuser = str(os.getenv("PG_DB"))
dbpassword = str(os.getenv("PG_PASS"))
dbname = str(os.getenv("PG_USER"))

ip = os.getenv("ip")

aiogram_redis = {
    'host': 5432,
}

redis = {
    'address': (ip,5432),
    'encoding': 'utf8'
}