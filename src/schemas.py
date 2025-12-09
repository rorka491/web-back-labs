from typing import TypeVar, Generic, Optional
from pydantic import BaseModel, Field, ConfigDict
from tortoise.contrib.pydantic import pydantic_model_creator
from src.models import Article, User
from enum import Enum
from datetime import datetime

T = TypeVar('T')


current_year = datetime.now().year

class Method(Enum):
    INFO = "info"
    BOOKING = "booking"
    CANCELATION = "cancelation"

class RegisterSchema(BaseModel):
    login: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=4)
    username: str = Field(..., min_length=2)


class LoginSchema(BaseModel):
    login: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    login: str

    class Config:
        from_attributes = True 


class ArticleSchema(BaseModel):
    author: UserOut
    title: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)
    is_favorite: bool
    is_public: bool

    model_config = {
        "from_attributes": True
    }

class OfficeCreate(BaseModel):
    title: str
    price: int
    is_booking: bool = False

class OfficeOut(BaseModel):
    id: int
    title: str
    is_booking: bool
    price: int
    tenant: Optional[UserOut] = None
    
    class Config:
        from_attributes = True

class OfficeList(BaseModel):
    office_list: list[OfficeOut]


class JsonRpcRequest(BaseModel):
    jsonrpc: str = "2.0"
    method: Method
    office_id: int = None


class JsonRpcResponse(BaseModel, Generic[T]):
    jsonrpc: str = "2.0"
    result: T


JsonRpcInfoResponse = JsonRpcResponse[OfficeList]
JsonRpcBookingResponse = JsonRpcResponse[OfficeOut]
JsonRpcCancelationResponse = JsonRpcResponse[OfficeOut]


class FilmOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    title_ru: str
    year: int
    description: str


class FilmCreate(BaseModel):
    title: str
    title_ru: str
    year: int = Field(..., ge=1895, le=current_year)
    description: str


class GiftOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    congrats: str
    url_photo: str
    is_opened: bool