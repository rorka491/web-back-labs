import datetime
from flask import Blueprint, render_template, url_for, redirect, request

lab1 = Blueprint("lab1", __name__, url_prefix="/lab1")


@lab1.route("/web")
def web():
    headers={
        'X-Server': 'sample',
        'Content-Type': 'text/plain; charset=utf-8'
    }
    return render_template("lab1/base.html"), 200, headers


@lab1.route("/author")
def get_author():
    data = {
        "name": "Родион",
        "group": "ФБИ 31",
        "faculty": "ФБ",
    }
    return render_template("lab1/author.html", data=data)


@lab1.route("/image")
def image():
    image_path = url_for("static", filename="ЯнТоплес.jpeg")
    data = {"image_path": image_path, "url_for": url_for}
    headers = {
        'X-Foo': 'Bar',
        'X-SpecialHeader': '1984',
        'Content-Language': 'ru' 
    }
    return render_template(data=data, image_path=image_path), 200, headers


count = 0


@lab1.route("/counter")
def counter():
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
    return render_template("lab1/counter.html", data=data), 200


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
    return render_template("lab1/create.html"), 201


@lab1.route('')
def title():
    return render_template("lab1/lab1.html")



