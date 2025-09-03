import datetime
from flask import Flask, redirect, request, url_for
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

environment = Environment(loader=FileSystemLoader("templates/"))


@app.route("/web")
def web():
    template = environment.get_template("base.html")
    return template.render()


@app.route("/author")
def get_author():
    template = environment.get_template("author.html")
    data = {
        "name": "Родион",
        "group": "ФБИ 31",
        "faculty": "ФБ",
    }
    return template.render(data)


@app.route("/image")
def image():
    template = environment.get_template("image.html")
    image_path = url_for("static", filename="ЯнТоплес.jpeg")
    data = {"image_path": image_path}
    return template.render(data)


count = 0

@app.route("/counter")
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

@app.route("/reset")
def clear_counter():
    global count
    count = 0
    return redirect(url_for('counter'))


