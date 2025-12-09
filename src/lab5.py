from quart import Blueprint, render_template, url_for, redirect, request, session, g, jsonify, send_file
from dataclasses import dataclass, asdict
from enum import Enum, unique
from src.models import User, Article, Video
from src.services.auth_service import AuthService, ValidationService
from src.schemas import LoginSchema, RegisterSchema, ArticleSchema, UserOut
from src.config import UPLOAD_DIR
from pydantic import ValidationError
from functools import wraps
import os
from src.services.hash_service import verify_password, hash_password

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
    return await render_template('lab5/index.html')


@lab5.route('/logout')
async def logout() -> str:
    session.pop('user')
    return redirect(url_for('lab5.index'))

@lab5.route('/list')
@login_required
async def list() -> str:
    articles_qs = await Article.all().select_related('author')\
        .filter(author=g.current_user)\
        .order_by('-is_favorite')
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
    is_favotite = form.get('is_favotite') or False
    is_public = form.get('is_public') or False

    await Article.create(
        title=title, 
        text=text, 
        author_id=author_id, 
        is_favotite=is_favotite, 
        is_public=is_public
    )

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
    


@lab5.route('/user_list')
@login_required
async def user_list() -> str:
    users_qs = await User.all()
    users = [UserOut.model_validate(a) for a in users_qs]
    return await render_template('lab5/table.html', users=users)


@lab5.route('/change_password', methods = ['GET', 'POST'])
@login_required
async def change_password() -> str:
    if request.method == HttpMethod.GET:
        return await render_template('lab5/change_pass.html', current_user=g.current_user)

    user = await User.get(username=g.current_user.username)

    form = await request.form
    username = form.get('username')
    password = form.get('password')
    password_confirm = form.get('password_confirm')

    if password != password_confirm:
        return await render_template('lab5/change_pass.html', error='Пароли должны совпадать')
    
    if password:
        user.password = hash_password(password)
    if username:
        user.username = username
    await user.save()

    return redirect(url_for('lab5.login'))


@lab5.post('/upload')
async def upload_video():
    form = await request.files
    file = form.get("file")

    if not file:
        return jsonify({"error": "No file"}), 400

    filepath = os.path.join(UPLOAD_DIR, file.filename)
    await file.save(filepath)

    await Video.create(title=file.filename, filename=file.filename)

    return redirect(url_for('lab5.index'))


@lab5.get("/media/videos/<filename>")
async def serve_video(filename):
    filepath = os.path.join(UPLOAD_DIR, filename)
    return await send_file(filepath)