from django.db import models
from user.models import User


class Interest(models.Model):
    text = models.CharField(max_length=255)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    property = models.ForeignKey('property.Property', on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False) 


    def __str__(self):
        return f"Интерес к {self.property.name} от {self.user.username}"
