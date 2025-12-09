from quart import Blueprint, render_template, url_for, redirect, request, session, g, jsonify, send_file, Request
from src.services.office_service import OfficeService
from src.schemas import FilmOut
from src.services.film_service import FilmService


lab8 = Blueprint("lab8", __name__, url_prefix="/lab8")


@lab8.get('/')
async def index():
    return await render_template('lab8/lab8.html')