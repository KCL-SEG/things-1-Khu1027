from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
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
            MaxValueValidator(100),
            MinValueValidator(0),
        ]
    )