from ninja import ModelSchema
from .models import Book


class BookListSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = '__all__'


class BookIdSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = '__all__'


class BookCreateSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = '__all__'
        exclude = ['id']