from tortoise import Tortoise, run_async
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")
DB_NAME = os.getenv("DB_NAME")
HOST_ADRESS = os.getenv("HOST_ADRESS")

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{DB_USER}:{DB_PASSWORD}@{HOST_ADRESS}/{DB_NAME}",
        "sqlite3": 'sqlite://db.sqlite3'
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    }
}



