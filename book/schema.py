from ninja import ModelSchema
from .models import Book


class BookIdSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = '__all__'