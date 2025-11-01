from typing import TYPE_CHECKING
from models import User
from schemas import LoginSchema, RegisterSchema, UserOut
from pydantic import ValidationError


if TYPE_CHECKING: 
    from quart import Request



class ValidationService:
    @staticmethod
    async def validate_login(request: "Request"):
        form = await request.form
        try:
            return LoginSchema(**form), None
        except ValidationError:
            return None, 'Заполните все поля'

    @staticmethod
    async def validate_register(request: "Request"):
        form = await request.form
        try:
            return RegisterSchema(**form), None
        except ValidationError:
            return None, 'Заполните все поля'
        
class AuthService:

    @staticmethod
    async def login_user(data: LoginSchema):
        user = await User.get_or_none(login=data.login)
        if not user or user.password != data.password:
            return None, 'Неверный логин или пароль'

        return UserOut.model_validate(user), None

    @staticmethod
    async def register_user(data: RegisterSchema) -> str|None:
        if await User.exists(login=data.login):
            return 'Пользователь уже существует'

        await User.create(**data.model_dump())
        return None
    
