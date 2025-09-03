from flask import Flask
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


