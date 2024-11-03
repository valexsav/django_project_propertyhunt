from django.db import models
from django.core.validators import MinValueValidator

from user.models import User

from PIL import Image


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
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Сначала вызываем родительский метод save, чтобы сохранить изображение
        super().save(*args, **kwargs)

        if self.photo:
            # Открываем изображение
            img = Image.open(self.photo.path)

            # Устанавливаем максимальные размеры
            max_width = 800
            max_height = 600

            # Проверяем, нужно ли изменять размер
            if img.width > max_width or img.height > max_height:
                # Пропорционально изменяем размер изображения
                img.thumbnail((max_width, max_height))
                
                # Сохраняем измененное изображение поверх исходного
                img.save(self.photo.path)
    

    def __str__(self):
        return f"name:{self.name} - location:{self.location} - price:{self.price} - area:{self.area}"


class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date_signed = models.DateField()
