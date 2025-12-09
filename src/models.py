from tortoise import Tortoise, fields, models

class BaseModelPK(models.Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True
    

    def __str__(self) -> str:
        return f'Object {self.__class__.__name__} ({self.id})'


class User(BaseModelPK):
    username = fields.CharField(max_length=255)
    login = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)

    class Meta: 
        table = 'users'

    def __str__(self):
        return f'{self.username} - {self.password}'


class Article(BaseModelPK):
    title = fields.CharField(max_length=255)
    text = fields.TextField()
    author = fields.ForeignKeyField('models.User', on_delete=fields.CASCADE)
    is_favorite = fields.BooleanField(default=False, )
    is_public = fields.BooleanField(default=False, null=True)

    class Meta: 
        table = 'articles'

    def __str__(self) -> str:
        return f'{self.title} - {self.author}'

class Human(BaseModelPK):
    name = fields.CharField(max_length=255)

    class Meta: 
        table = 'human'
    
class Video(BaseModelPK):
    title = fields.CharField(max_length=100)
    filename = fields.CharField(max_length=255)
    uploaded_at = fields.DatetimeField(auto_now_add=True)

    class Meta: 
        table = 'videos'

    def __str__(self):
        return f'{self.title} - {self.uploaded_at}'
    

class Film(BaseModelPK):
    title = fields.CharField(max_length=255)
    title_ru = fields.CharField(max_length=255)
    year = fields.IntField(max_length=4)
    description = fields.CharField(max_length=2000)

    class Meta:
        table = "films"

class Gift(BaseModelPK):
    url_photo = fields.CharField(max_length=3000)
    congrats = fields.CharField(max_length=255)
    is_opened = fields.BooleanField(default=False)

    class Meta:
        table = "gifts"



class Office(BaseModelPK):
    title = fields.CharField(max_length=255, null=True)
    is_booking = fields.BooleanField(default=False)
    price = fields.IntField()
    tenant = fields.ForeignKeyField('models.User', on_delete=fields.CASCADE, default=None, null=True)

    class Meta:
        table = 'offices'
    
    def __str__(self):
        return f'{self.title} - {self.is_booking}'


