from flask import Blueprint, render_template, url_for, redirect, request, abort, make_response

lab3 = Blueprint("lab3", __name__, url_prefix="/lab3")


@lab3.route("/")
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color)



@lab3.route("/cookie")
def cookie():
    response = make_response(redirect('/lab3/'))
    response.set_cookie('name', 'Rodion', max_age=10)
    response.set_cookie('age', '20')
    response.set_cookie('color', 'magenta')
    return response



@lab3.route("/del_cookie")
def del_cookie():
    response = make_response(redirect('/lab3/'))
    response.delete_cookie('name')
    response.delete_cookie('age')
    response.delete_cookie('color')
    return response


@lab3.route("/form1")
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните анкету'
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, sex=sex, age=age, errors=errors)

@lab3.route("/order")
def order():
    drink = request.args.get('drink')
    milk = request.args.get('milk')
    sugar = request.args.get('sugar')
    return render_template('lab3/order.html', drink=drink, sugar=sugar, milk=milk)

@lab3.route("/pay")
def pay():
    drink_map = {
        "coffee": 100,
        "black-tea": 120,
        "green-tea": 110,
        "sugar": 10,
        "milk": 20
    }
    price = 0
    drink = request.args.get("drink")
    price = drink_map.get(drink, 0)

    if "milk" in request.args:
        price += drink_map["milk"]
    if "sugar" in request.args:
        price += drink_map["sugar"]
    return render_template('/lab3/pay.html', price=price)

@lab3.route("/success")
def success():
    return make_response('Успех')

@lab3.route("/settings")
def settings():
    color = request.args.get('color')
    
    if color:
        response = make_response(redirect('/lab3/settings'))
        response.set_cookie('color', color)
        return response

    color = request.cookies.get('color')
    response = make_response(render_template('lab3/settings.html', color=color))
    
    return response

