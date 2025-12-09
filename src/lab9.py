from quart import Blueprint, render_template, url_for, redirect, request, session, g, jsonify, send_file, Request
from src.services.office_service import OfficeService
from src.schemas import FilmOut
from src.services.film_service import FilmService
from src.schemas import GiftOut
from src.services.gift_service import GiftService
from functools import wraps
from src.exception import UserUnauthorized


def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        user = session.get('user')
        if not user:
            raise UserUnauthorized()
        return await func(*args, **kwargs)
    return wrapper


lab9 = Blueprint("lab9", __name__, url_prefix="/lab9")

gift_service = GiftService()

@lab9.get('/')
async def index():
    return await render_template('lab9/lab9.html')


@lab9.get('/api/gifts')
async def gifts() -> list[GiftOut]:
    gifts = await gift_service.get_all()
    return gifts

@lab9.post("/api/gifts/open/<int:id>")
@login_required
async def open_gift(id: int):
    opened_count = session.get("opened_gifts_count", 0)
    # if opened_count >= 3:
    #     return {"detail": "Жадина оставь другим"}, 403
    
    gift = await gift_service.open_gift(id=id)
    session["opened_gifts_count"] = opened_count + 1

    return gift

@lab9.post("/api/gifts/restore")
async def restore_gifts():
    await gift_service.restore_gifts()
    return {"detail": "success"}





