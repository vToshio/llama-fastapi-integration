from tortoise.models import Model
from tortoise import fields

class UserModel(Model):
    id = fields.IntField(pk=True)
    nome = fields.CharField(max_length=100, nullable=False)

    class Meta:
        table = 'users'