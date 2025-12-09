from quart import Quart, render_template
from src.lab1 import lab1
from src.lab2 import lab2
from src.lab3 import lab3
from src.lab4 import lab4
from src.lab5 import lab5
from src.lab6 import lab6
from src.lab7 import lab7
from src.lab8 import lab8
from src.lab9 import lab9
from src.config import TORTOISE_ORM, UPLOAD_DIR, TEMPLATE_DIR, STATIC_DIR
import os
from dotenv import load_dotenv
from tortoise.contrib.quart import register_tortoise
from quart import session, g, request
from src.models import User

load_dotenv() 


app = Quart(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

os.makedirs(UPLOAD_DIR, exist_ok=True)
app.secret_key = os.getenv('SECRET_KEY') 
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)

@app.before_request
async def load_current_user() -> None:
    user_data = session.get("user")
    if user_data:
        g.current_user = await User.get_or_none(login=user_data.get("login"))



@app.before_request
async def save_current_endpoint():
    g.current_endpoint = request.endpoint

@app.context_processor
def inject_current_endpoint():
    return {"current_endpoint": getattr(g, "current_endpoint", "")}

@app.route("/")
async def index():
    return await render_template("index.html"), 200


@app.route("/400")
def bad_request():
    return "400 Bad Request", 400


@app.route("/401")
def unauthorized():
    return "401 Unauthorized", 401


@app.route("/402")
def payment_required():
    return "402 Payment Required", 402


@app.route("/403")
def forbidden():
    return "403 Forbidden", 403


@app.route("/405")
def method_not_allowed():
    return "405 Method Not Allowed", 405


@app.route("/418")
def teapot():
    return "418 I'm a teapot", 418


@app.errorhandler(500)
def internal_error(error):
    return "На сервере произошла ошибка. Попробуйте позже.", 500


@app.route("/crash")
def crash():
    1 / 0
