import factory
from factory.declarations import SubFactory

from ..models import Stock, Quote


class StockFactory(factory.django.DjangoModelFactory):
    code = factory.Faker("first_name")
    name = factory.Faker("sentence", nb_words=2)
    logo = factory.Faker("file_name", category="image")
    sector = factory.Faker("sentence", nb_words=1)

    class Meta:
        model = Stock

class QuoteFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('pricetag')
    stock = SubFactory(StockFactory)

    class Meta:
        model = Quote