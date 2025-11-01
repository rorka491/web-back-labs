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

    class Meta: 
        table = 'articles'

    def __str__(self) -> str:
        return f'{self.title} - {self.author}'
    




