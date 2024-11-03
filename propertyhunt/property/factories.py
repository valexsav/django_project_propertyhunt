import factory
from factory import Faker
from .models import Property
import random
from factory.fuzzy import FuzzyInteger


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property
        django_get_or_create = ('name',)

    name = Faker('text', max_nb_chars=20)
    
    # Указываем диапазон значений для случайного целого числа
    price = factory.fuzzy.FuzzyInteger(2000000, 10000000)
    
    # Используем предопределённые значения из списка для поля location
    location = Faker('address', locale='pl_PL')
    # location = factory.LazyAttribute(lambda _: random.choice(['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург']))
    
    # Используем Faker для генерации случайного целого числа для площади
    area = factory.fuzzy.FuzzyInteger(20, 1000)

    owner_id = 1
