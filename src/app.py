import datetime
from flask import Flask, redirect, render_template, request, url_for, Blueprint, abort
from jinja2 import Environment, FileSystemLoader



app = Flask(__name__)


environment = Environment(loader=FileSystemLoader("templates/"))


@app.route("/")
@app.route("/index")
def index():
    template = environment.get_template("index.html")
    return template.render(), 200


lab1 = Blueprint("lab1", __name__, url_prefix="/lab1")
lab2 = Blueprint("lab2", __name__, url_prefix="/lab2")


@lab1.route("/web")
def web():
    template = environment.get_template("base.html")
    headers={
        'X-Server': 'sample',
        'Content-Type': 'text/plain; charset=utf-8'
    }
    return template.render(), 200, headers


@lab1.route("/author")
def get_author():
    template = environment.get_template("author.html")
    data = {
        "name": "Родион",
        "group": "ФБИ 31",
        "faculty": "ФБ",
    }
    return template.render(data)


@lab1.route("/image")
def image():
    template = environment.get_template("image.html")
    image_path = url_for("static", filename="ЯнТоплес.jpeg")
    data = {"image_path": image_path, "url_for": url_for}
    headers = {
        'X-Foo': 'Bar',
        'X-SpecialHeader': '1984',
        'Content-Language': 'ru' 
    }
    return template.render(data), 200 , headers 


count = 0


@lab1.route("/counter")
def counter():
    template = environment.get_template("counter.html")
    global count
    count += 1
    url = request.url
    client_ip = request.remote_addr
    time = datetime.datetime.today()
    data = {
        "count": count, 
        "time": str(time), 
        "client_ip": client_ip, 
        "url": url
    }
    return template.render(data)


@lab1.route("/reset")
def clear_counter():
    global count
    count = 0
    return redirect(url_for("lab1.counter"))


@lab1.route("/info")
def info():
    return redirect("/lab1/author")


@lab1.route("/created")
def created():
    template = environment.get_template("create.html")
    return template.render(), 201


@lab1.route('')
def title():
    template = environment.get_template("lab1.html")
    return template.render()


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



@lab2.route("/")
@lab2.route("/index")
def index():
    return render_template("lab2.html", lab_num=3, name="Родион")

@lab2.route("/a")
def without_slash():
    return "Без слэша"


@lab2.route("/a/")
def with_slash():
    return "С слешем"

flower_list = [
    "Навоз",
    "Навоз",
    "Роза",
    "Навоз",
    "Навоз",
]

@lab2.route("/flowers/<int:flower_id>")
def flowers(flower_id):
    global flower_list
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return f"цветок {flower_list[flower_id]}"

@lab2.route("/add_flower/<string:name>")
def add_flower(name):
    global flower_list

    flower_list.append(name)
    return f"""
        Всего цветов {len(flower_list)}
        Полный список {flower_list}
    """

@lab2.route("/example")
def example() -> str:
    fruits = ["Груша", "Яблоко", "Арбуз", "Дыня", "Апельсин", "Огурец"]
    fruits = [
        {"name": "Груша", "price": 100},
        {"name": "Яблоко", "price": 120},
        {"name": "Арбуз", "price": 130},
        {"name": "Дыня", "price": 90},
        {"name": "Апельсин", "price": 70},
        {"name": "Огурец", "price": 200},
    ]
    return render_template("example.html", name="Родион", fruits=fruits)



app.register_blueprint(lab1)
app.register_blueprint(lab2)