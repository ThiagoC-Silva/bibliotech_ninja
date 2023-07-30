from ninja import Router
from typing import List
from .schema import BookListSchema, BookIdSchema, BookCreateSchema, BookUpdateSchema
from .models import Book
from django.shortcuts import get_object_or_404


router = Router()


@router.get('list/', response = List[BookListSchema])
def list(request):
    book_list = Book.objects.all()
    return book_list


@router.get('{book_id}/', response = BookIdSchema)
def search_book(request, book_id: int):
    book = get_object_or_404(Book, id = book_id)
    return book


@router.post('new_book/')
def create_book(request, new_book: BookCreateSchema):
    book = Book.objects.create(**new_book.dict())
    return {'Sucess': True}


@router.put('update_book/{book_id}/')
def book_update(request, book_id: int, update: BookUpdateSchema ):
    book = get_object_or_404(Book, id = book_id) 
    for attr, value in update.dict().items():
        setattr(book, attr, value)
    book.save()
    return {'Sucess': True}


@router.delete('delete_book/{book_id}/')
def book_delete(request, book_id: int):
    book = get_object_or_404(Book, id = book_id)
    book.delete()
    return {'Sucess': True}