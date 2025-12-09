from quart import Blueprint, render_template, redirect, request, abort, session
from dataclasses import dataclass, asdict

lab4 = Blueprint("lab4", __name__, url_prefix="/lab4")

@dataclass
class User: 
    login: str
    password: str
    username: str

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "User":
        return User(**data)




async def get_int(name: str, default=0) -> int:
    try:
        return int(await request.form.get(name))
    except (TypeError, ValueError):
        return default
    
def get_result(x1, x2, operation="div") -> float | str:
    match operation: 
        case 'sum': result = x1 + x2
        case 'dif': result = x1 - x2
        case 'mult': result = x1 * x2
        case 'div':
            try: 
                result = x1 / x2
            except ZeroDivisionError:
                return 'Ошибка деление на 0'
        case 'exp': result = x1 ** x2
    
    return result

typeError = str

async def clean_form(form: dict) -> typeError:
    x1 = await form.get('x1') 
    x2 = await form.get('x2')
    if not x1 or not x2: 
        return 'Поля формы должны быть заполены'


@lab4.route('/')
async def lab() -> str:
    return await render_template('lab4/lab4.html')


operations_mapping = {
    "sum": "+",
    "dif": "-",
    "mult": "*",
    "div": "/",
    "exp": "**",
}

@lab4.route('/<string:operation>')
async def view_form(operation) -> str:
    if operation not in operations_mapping:
        abort(404)

    return await render_template(
        f'lab4/math-form.html', 
        operation=operation, 
        operations_mapping=operations_mapping
    )


@lab4.route('/<string:operation>', methods=['POST'])
async def operation_handler(operation):
    form = request.form
    error = clean_form(form)
    if error: 
        return await render_template('/lab4/result.html', error=error)

    x1 = get_int('x1')
    x2 = get_int('x2')
    result = get_result(x1, x2, operation=operation)

    return await render_template('/lab4/result.html', x1=x1, x2=x2, result=result, operation=operations_mapping[operation])

tree_count = 0

@lab4.route('/tree', methods=["GET", "POST"])
async def tree():
    global tree_count
    if request.method == 'GET': 
        return await render_template('lab4/tree.html', tree_count=tree_count)
    
    form = await request.form
    operation = form.get('operation')

    match operation: 
        case 'cut': tree_count -= 1
        case 'plant': tree_count += 1

    return redirect('/lab4/tree')



users = {
    1: User('Rodion', '123', 'Родион Горшков'),
    2: User('Dmitriy', '321', 'Дмитрий Михеев')
}

async def check_credentials(login: str, password: str) -> User | None:
    for user in users.values(): 
        if user.login == login and user.password == password:
            return user
    return None


@lab4.route('/login', methods=['GET', 'POST'])
async def login():
    error = ''
    login = ''
    password = ''
    authorized = False

    if request.method == 'GET':
        if 'login' in session: 
            authorized = True
            login = session['login']
        return await render_template(
            '/lab4/login.html',
            authorized=authorized, 
            login=login,
            password=password,
        )
    
    #POST

    form = await request.form
    login = form.get('login')
    password = form.get('password')
    
    user = await check_credentials(login, password)
    if user:
        session['user'] = user.to_dict()
        authorized = True
        return await render_template(
            '/lab4/login.html', 
            authorized=True, 
            login=login, 
            password=password, 
        )

    error = 'Неверный логин или пароль'
    return await render_template('/lab4/login.html', error=error, authorized=authorized)

@lab4.route('/logout', methods=['POST'])
def logout(): 
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/fridge', methods=['GET', 'POST'])
async def fridge():
    form = await request.form
    message = ''
    snowflakes = 0
    temperature = form.get('temperature')

    if request.method == 'POST':
        if not temperature:
            message = 'Ошибка: не задана температура'
        else:
            try:
                t = int(temperature)
                if t < -12:
                    message = 'Не удалось установить температуру — слишком низкое значение'
                elif t > -1:
                    message = 'Не удалось установить температуру — слишком высокое значение'
                elif -12 <= t <= -9:
                    message = f'Установлена температура: {t}°C'
                    snowflakes = 3
                elif -8 <= t <= -5:
                    message = f'Установлена температура: {t}°C'
                    snowflakes = 2
                elif -4 <= t <= -1:
                    message = f'Установлена температура: {t}°C'
                    snowflakes = 1
            except ValueError:
                message = 'Ошибка: температура должна быть числом'

    return await render_template(
        'lab4/fridge.html',
        message=message,
        snowflakes=snowflakes
    )


@lab4.route('/grain', methods=['GET', 'POST'])
async def grain():
    prices = {
        'ячмень': 12000,
        'овёс': 8500,
        'пшеница': 9000,
        'рожь': 15000
    }

    message = ''
    discount_message = ''
    total = 0

    if request.method == 'POST':
        form = await request.form
        grain = form.get('grain')
        weight = form.get('weight')

        if not grain or grain not in prices:
            message = 'Ошибка: не выбрано зерно'
        elif not weight:
            message = 'Ошибка: не указан вес'
        else:
            try:
                weight = float(weight)
                if weight <= 0:
                    message = 'Ошибка: вес должен быть больше 0'
                elif weight > 100:
                    message = 'Такого объёма сейчас нет в наличии'
                else:
                    price = prices[grain]
                    total = price * weight
                    if weight > 10:
                        discount = total * 0.1
                        total -= discount
                        discount_message = f'Применена скидка 10% за большой объём (-{discount:,.0f} руб)'
                    message = (
                        f'Заказ успешно сформирован. '
                        f'Вы заказали {grain}. Вес: {weight} т. '
                        f'Сумма к оплате: {total:,.0f} руб.'
                    )
            except ValueError:
                message = 'Ошибка: вес должен быть числом'

    return await render_template(
        'lab4/grain.html',
        message=message,
        discount_message=discount_message
    )




