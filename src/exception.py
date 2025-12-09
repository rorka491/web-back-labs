from werkzeug.exceptions import HTTPException


class BusinessError(HTTPException):
    code = 400

class OfficeAlreadyBookedError(BusinessError):
    code = 409
    description = "Офис уже забронирован"

class OfficeNotRentedByUserError(BusinessError):
    code = 403
    description = "Вы не арендуете этот офис"

class OfficeNotFound(BusinessError):
    code = 404
    description = 'Офис не надйен'

class UserUnauthorized(BusinessError):
    code = 401
    description = "Пользователь не авторизован"

class FilmNotFound(BusinessError):
    code = 404
    description = "Фильм не найден"


class LoginRequired(BusinessError):
    code = 401
    description = "Пользователь не авторизован"


class GiftAlreadyOpened(BusinessError):
    code = 418
    description = 'Подарок уже открыт'

class GiftNotFound(BusinessError):
    code = 404
    description = 'Подарок не надйен'