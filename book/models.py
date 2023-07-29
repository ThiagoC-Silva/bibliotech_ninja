from django.db import models


class Book(models.Model):
    title = models.CharField(max_length = 35)
    author = models.CharField(max_length = 20)
    publication_year = models.IntegerField()
    publishing_company = models.CharField(max_length = 15)

    def __str__(self):
        return self.title