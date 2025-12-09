from tortoise import Tortoise, run_async
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")
DB_NAME = os.getenv("DB_NAME")
HOST_ADRESS = os.getenv("HOST_ADRESS")
DB_TYPE = os.getenv('DB_TYPE')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "src", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "src", "static")
UPLOAD_DIR = "media/videos"
sqlite_path = os.path.join(BASE_DIR, "db.sqlite3")

connect_maping = {
    "postgres": f"postgres://{DB_USER}:{DB_PASSWORD}@{HOST_ADRESS}/{DB_NAME}",
    "sqlite3": f'sqlite://{sqlite_path}'
}

TORTOISE_ORM = {
    "connections": {
        "default": connect_maping.get(DB_TYPE, connect_maping["sqlite3"])
    },
    "apps": {
        "models": {
            "models": ["src.models", "aerich.models"],
            "default_connection": "default",
        }
    }
}



