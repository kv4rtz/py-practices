from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    image = models.ImageField(upload_to='book/%Y/%m/%d')