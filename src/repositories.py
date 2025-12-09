from typing import TypeVar
from abc import ABC, abstractmethod
from src.models import BaseModelPK, Office, User, Film, Gift 
from tortoise.queryset import QuerySet

M = TypeVar('M', bound=BaseModelPK)

class AbstractRepository(ABC):
    model: type[M] = None



    @abstractmethod
    async def get_all(self) -> list[M]:
        raise NotImplementedError
    
    @abstractmethod
    async def get_object(self, **filters) -> M | None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, obj: M, **update_data)  -> M:
        raise NotImplementedError


class TortoiseRepository(AbstractRepository): 
    async def get_all(self, *prefetch) -> list[M]:
        return await self.model.all().prefetch_related(*prefetch)

    async def get_object(self, *prefetch, **filters) -> M | None:
        return await self.model.get_or_none(**filters).prefetch_related(*prefetch)
        
    async def update(self, obj: M, **update_data) -> M:
        for field, value in update_data.items():
            setattr(obj, field, value)
        await obj.save()
        return obj
    
    async def bulk_update(self, objs: list[M], fields: list[str]):
        await self.model.bulk_update(objs, fields)
    
    async def delete(self, obj: M) -> None:
        await obj.delete()

    async def create(self, **create_data):
        obj = await self.model.create(**create_data)
        return obj


class UserRepository(TortoiseRepository):
    model = User

class OfficeRepository(TortoiseRepository):
    model = Office


class FilmRepository(TortoiseRepository):
    model = Film

class GiftRepository(TortoiseRepository):
    model = Gift


