from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=50)
    egs = models.FloatField()
    breed = models.CharField(max_length=50)
    entry_date = models.DateField()
