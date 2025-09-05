import datetime
from flask import Flask, redirect, request, url_for, Blueprint
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)


environment = Environment(loader=FileSystemLoader("templates/"))


@app.route("/")
@app.route("/index")
def index():
    template = environment.get_template("index.html")
    return template.render(), 200


lab1 = Blueprint("lab1", __name__, url_prefix="/lab1")


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
    return template.render(data)


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
    return redirect(url_for('counter'))


@lab1.route("/info")
def info():
    return redirect("/author")


@lab1.route("/created")
def created():
    template = environment.get_template("create.html")
    return template.render(), 201


@lab1.errorhandler(404)
def not_found(error):
    template = environment.get_template("error404.html")

    return template.render(), 404

@lab1.route('')
def title():
    template = environment.get_template("lab1.html")
    return template.render()

app.register_blueprint(lab1)

                                                    


                                