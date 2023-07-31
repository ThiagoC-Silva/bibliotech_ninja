from ninja import Router
from typing import List
from .schema import BookSchema, BookCreateSchema, BookIdSchema
from .models import Book
from django.shortcuts import get_object_or_404


router = Router()


@router.get('book/', response = List[BookSchema])
def list(request):
    return Book.objects.all()


@router.get('book/{book_id}/', response = BookSchema)
def search_book(request, book_id: int):
    return get_object_or_404(Book, id = book_id)
    


@router.post('book/')
def create_book(request, new_book: BookCreateSchema):
    Book.objects.create(**new_book.dict())
    return {'Sucess': True}


@router.put('book/{book_id}/')
def book_update(request, book_id: int, update: BookIdSchema ):
    book = get_object_or_404(Book, id = book_id) 
    for attr, value in update.dict().items():
        setattr(book, attr, value)
    book.save()
    return {'Sucess': True}


@router.delete('book/{book_id}/')
def book_delete(request, book_id: int):
    book = get_object_or_404(Book, id = book_id)
    book.delete()
    return {'Sucess': True}