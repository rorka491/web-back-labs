from flask import Blueprint, render_template, url_for, redirect, request, abort

lab2 = Blueprint("lab2", __name__, url_prefix="/lab2")



@lab2.route("/")
@lab2.route("/index")
def index():
    return render_template("lab2/lab2.html", lab_num=3, name="Родион")

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

@lab2.route("/flowers")
def all_flowers():
    global flower_list

    return f"{flower_list}"


@lab2.route("/delete_flowers")
def delete_flowers():
    global flower_list
    flower_list.clear()

    return redirect("/lab2/flowers")


@lab2.route("/flowers/<int:flower_id>")
def flowers(flower_id):
    global flower_list
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return f"""
        цветок {flower_list[flower_id]}
        <a href="http://127.0.0.1:5000/lab2/flowers">Все цветы</a>
        """

@lab2.route("/add_flower/", defaults={"name": None})
@lab2.route("/add_flower/<string:name>")
def add_flower(name):
    global flower_list

    if not name:
        abort(400)

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
    return render_template("lab2/example.html", name="Родион", fruits=fruits)

@lab2.route("/filters")
def filters():
    phrase = "<h1>Это уже <i>было</i> в симпсонах</h1>"
    return render_template('lab2/filters.html', phrase=phrase)

@lab2.route("/calc/", defaults={"a": 1, "b": 1})
@lab2.route("/calc/<int:a>/", defaults={"b": 1})
@lab2.route("/calc/<int:a>/<int:b>/")
def math_operations(a, b):
    
    result = {
        "sum": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b != 0 else "На 0 делить нельзя",
        "pow": a ** b
    }
    return render_template("lab2/math.html", a=a, b=b, result=result)



