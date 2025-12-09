from quart import Blueprint, render_template, url_for, redirect, request, session, g, jsonify, send_file, Request
from src.services.office_service import OfficeService
from src.schemas import FilmOut
from src.services.film_service import FilmService


lab7 = Blueprint("lab7", __name__, url_prefix="/lab7")

film_service = FilmService()

@lab7.get('/')
async def index():
    return await render_template('lab7/lab7.html')

# @lab7.get('/form')
# async def create_form():
#     return await render_template('lab7/create_form.html')

@lab7.get('/api/films/<int:id>')
async def get_film(id: int) -> FilmOut:
    film = await film_service.get_film_by_id(id)
    return FilmOut.model_validate(film).model_dump()

@lab7.delete('/api/films/<int:id>')
async def delete_film(id: int):
    await film_service.delete_film_by_id(id)
    return {"detail": "success"}

@lab7.patch('/api/films/<int:id>')
async def update_film(id: int): 
    updated_film = await film_service.update_film(id=id, request=request)
    return FilmOut.model_validate(updated_film).model_dump()

@lab7.post('/api/films')
async def create_film():
    created_film = await film_service.create_film(request=request)
    return FilmOut.model_validate(created_film).model_dump()


@lab7.get('/api/films')
async def list_films() -> list[FilmOut]:
    films = await film_service.all_films()
    return [FilmOut.model_validate(film).model_dump() for film in films]

