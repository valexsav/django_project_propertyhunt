from ..models import Property
import factory.fuzzy


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    name = factory.Faker('text', max_nb_chars=20)
    price = factory.fuzzy.FuzzyInteger(2000000, 10000000)
    location = factory.Faker('address', locale='pl_PL')
    area = factory.fuzzy.FuzzyInteger(20, 1000)
    owner = factory.SubFactory('user.tests.factories.OwnerFactory')
    description = factory.Faker('sentence', nb_words=20)
