from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from property.models import Property


class PropertyInline(admin.StackedInline):
    model = Property
    extra = 0


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [PropertyInline]
