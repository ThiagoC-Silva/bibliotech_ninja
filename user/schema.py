from ninja import ModelSchema
from .models import User


class UserSchema(ModelSchema):
    class Config():
        model = User
        model_fields = '__all__'


class UserCreateSchema(ModelSchema):
    class Config():
        model = User
        model_fields = ('name', 'birth', 'cpf', 'email')

class UserUpdateSchema(ModelSchema):
    class Config():
        model = User
        model_fields = ('name', 'birth', 'cpf', 'email')
        