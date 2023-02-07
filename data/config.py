import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))


admins = [
    294349333
]

# dbuser = str(os.getenv("PG_DB"))
# dbpassword = str(os.getenv("PG_PASS"))
# dbname = str(os.getenv("PG_USER"))

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