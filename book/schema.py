from ninja import ModelSchema
from .models import Book


class BookSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = '__all__'

class BookCreateSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = ('title', 'author', 'publication_year', 'publishing_company')


class BookIdSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = ('title', 'author', 'publication_year', 'publishing_company')