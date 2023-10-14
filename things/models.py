from django.db import models
from django.db.models import Model
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Thing(Model):
    name = models.TextField(
        unique=True,
        blank=False,
        max_length=30,
    )
    description = models.TextField(
        unique=False,
        blank=True,
        max_length=120,
    )
    quantity = models.IntegerField(
        unique=False,
        validators=[
            MaxLengthValidator(100),
            MinLengthValidator(0),
        ]
    )