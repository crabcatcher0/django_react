from django.db import models

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length = 20)
    author = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='prodimages/')