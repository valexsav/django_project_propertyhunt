from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):

    OWNER_OR_BUYER_CHOICES = [
        ('OWNER', 'Owner'),
        ('BUYER', 'Buyer'),
    ]

    role = models.CharField(
        max_length=5,
        choices=OWNER_OR_BUYER_CHOICES,
        default='BUYER'
    )
    