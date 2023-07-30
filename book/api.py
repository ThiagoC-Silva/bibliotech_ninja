from ninja import NinjaAPI
from typing import List
from .schema import BookListSchema, BookIdSchema, BookCreateSchema
from .models import Book
from django.shortcuts import get_object_or_404


api = NinjaAPI()


@api.get('list/', response = List[BookListSchema])
def list(request):
    book_list = Book.objects.all()
    return book_list


@api.get('{book_id}/', response = BookIdSchema)
def search_book(request, book_id: int):
    book = get_object_or_404(Book, id = book_id)
    return book


@api.post('new_book/')
def create_book(request, new_book: BookCreateSchema):
    book = Book.objects.create(**new_book.dict())
    return 'Novo livro cadastrado com sucesso!'