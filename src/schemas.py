from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator
from models import Article, User



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

    model_config = {
        "from_attributes": True
    }