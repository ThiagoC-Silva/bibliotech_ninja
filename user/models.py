from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 80)
    birth = models.DateField()
    cpf = models.CharField(max_length = 11)
    email = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
