import datetime
from flask import Flask, redirect, render_template, request, url_for, Blueprint, abort
from jinja2 import Environment, FileSystemLoader
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html"), 200


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





