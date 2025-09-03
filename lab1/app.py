from flask import Flask, url_for
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

environment = Environment(loader=FileSystemLoader("templates/"))

@app.route("/web")
def web():
    template = environment.get_template('base.html')
    return template.render()


@app.route('/author') 
def get_author():
    template = environment.get_template("author.html")
    data={
        "name": "Родион",
        "group": "ФБИ 31",
        "faculty": "ФБ",
    }                  
    return template.render(data)

@app.route('/image')
def image():
    template = environment.get_template("image.html")
    image_path = url_for("static", filename="ЯнТоплес.jpeg")
    data = {
        "image_path": image_path
    }
    return template.render(data)
