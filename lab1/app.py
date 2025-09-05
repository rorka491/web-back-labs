import datetime
from flask import Flask, redirect, request, url_for
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

environment = Environment(loader=FileSystemLoader("templates/"))


@app.route("/web")
def web():
    template = environment.get_template("base.html")
    headers={
        'X-Server': 'sample',
        'Content-Type': 'text/plain; charset=utf-8'
    }
    return template.render(), 200, headers


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
    data = {"image_path": image_path, "url_for": url_for}
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


@app.route('/info')
def info():
    return redirect("/author")


@app.route('/created')
def created():
    template = environment.get_template("create.html")
    return template.render(), 201


@app.errorhandler(404)
def not_found(error):
    template = environment.get_template("error404.html")
    
    return template.render(), 404



