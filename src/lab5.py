from quart import Blueprint, render_template, url_for, redirect, request, abort, make_response, session
from dataclasses import dataclass, asdict
from enum import Enum, unique
from models import User, Article
from services.auth_service import AuthService, ValidationService
from schemas import LoginSchema, RegisterSchema, ArticleSchema
from pydantic import ValidationError
from functools import wraps

lab5 = Blueprint("lab5", __name__, url_prefix="/lab5")

def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        user = session.get('user')
        if not user:
            return redirect(url_for('lab5.login'))
        return await func(*args, **kwargs)
    return wrapper


class HttpMethod:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


@lab5.route('/')
async def index() -> str: 
    return await render_template('lab5/lab5.html')


@lab5.route('/logout')
async def logout() -> str:
    session.pop('user')
    return redirect(url_for('lab5.index'))

@lab5.route('/list')
@login_required
async def list() -> str:
    articles_qs = await Article.all().select_related('author').filter(author__login=login) # решает проблему n+1
    articles = [ArticleSchema.model_validate(a) for a in articles_qs]
    return await render_template('lab5/list.html', articles=articles)


@lab5.route('/create', methods = ['GET', 'POST'])
@login_required
async def create() -> str:
    if request.method == HttpMethod.GET: 
        return await render_template('lab5/create.html')

    form = await request.form
    title = form.get('title') 
    text = form.get('text')
    author_id = session['user']['id']

    await Article.create(title=title, text=text, author_id=author_id)

    return redirect(url_for('lab5.list'))



@lab5.route('/login', methods = ['GET', 'POST'])
async def login() -> str:
    if request.method == HttpMethod.GET:
        return await render_template('lab5/login.html')

    data, error = await ValidationService.validate_login(request)
    if not error: 
        user, error = await AuthService.login_user(data)

    if error:
        return await render_template('lab5/login.html', error=error)
    
    session['user'] = user.model_dump()
    return redirect(url_for('lab5.index'))


@lab5.route('/register', methods = ['GET', 'POST'])
async def register() -> str:
    if request.method == HttpMethod.GET:
        return await render_template('lab5/register.html')

    data, error = await ValidationService.validate_register(request)
    if not error:
        error = await AuthService.register_user(data)
    
    if error: 
        return await render_template('lab5/register.html', error=error)

    return redirect(url_for('lab5.login'))
    


