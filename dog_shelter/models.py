from datetime import date
from django.core.exceptions import ValidationError
from django.db import models


def date_control(value):
    today = date.today()
    if value != today:
        raise ValidationError('Дата добавления животного в базу может быть только текущей!')


class Dog(models.Model):
    name = models.CharField(max_length=50)
    egs = models.FloatField()
    breed = models.CharField(max_length=50)
    entry_date = models.DateField(validators=[date_control])

    def __str__(self):
        return self.name
