from django.db import models

from django.core.validators import MinValueValidator

from user.models import User


class Property(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(
        null=False,
        validators=[
            MinValueValidator(0)
        ]
    )
    location = models.CharField(max_length=50)
    area = models.IntegerField(
        null=False,
        validators=[
            MinValueValidator(0)
        ],
    )
    owner = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='properties_owned',
        )
    buyer = models.ManyToManyField(
        'user.User',
        through='Contract', 
        related_name='properties_to_buy',
        )


class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date_signed = models.DateField()
