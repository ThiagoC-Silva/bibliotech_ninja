from django.db import models
from book.models import Book
from user.models import User


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()


    def __str__(self):
        return f'{self.book.title} - {self.user.name}'