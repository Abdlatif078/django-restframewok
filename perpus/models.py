from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    isbn = models.CharField(max_length=13)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

