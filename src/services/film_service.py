from typing import TYPE_CHECKING
from src.models import User
from src.schemas import LoginSchema, RegisterSchema, UserOut
from pydantic import ValidationError
from .hash_service import verify_password, hash_password
from src.repositories import FilmRepository
from src.schemas import FilmOut, FilmCreate
from quart import Request
from src.exception import FilmNotFound
from src.repositories import M

class FilmService:
    repo = FilmRepository()

    async def all_films(self) -> list[M]:
        films = await self.repo.get_all()
        return films
    
    async def get_film_by_id(self, id) -> M:
        film = await self.get_film_or_exception(id=id)
        return film
    
    async def get_film_or_exception(self, **filters) -> M:
        film = await self.repo.get_object(**filters)
        if not film:
            raise FilmNotFound()
        return film
    
    async def delete_film_by_id(self, id: int) -> None:
        film = await self.get_film_or_exception(id=id)
        await self.repo.delete(film)

    async def update_film(self, id: int, request: Request) -> M:
        data: dict = await request.get_json()
        film_data = FilmCreate.model_validate(data).model_dump()
        film = await self.repo.get_object(id=id)
        updated_film = await self.repo.update(obj=film, **film_data)
        return updated_film

    async def create_film(self, request: Request) -> M:
        data: dict = await request.get_json()
        film_data = FilmCreate.model_validate(data).model_dump()
        created_film = await self.repo.create(**film_data)
        return created_film


    




