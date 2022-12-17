import pytest

from ..models import Stock, Quote
from .factories import StockFactory, QuoteFactory

pytestmark = pytest.mark.django_db

class TestStockModel:
    def test_create_stock(self):
        stock = Stock.objects.create(
            code='ABC1',
            name='Abstract Basic',
            logo='logo.svg',
            sector='development')
        assert stock.code == 'ABC1'
        assert stock.name == 'Abstract Basic'
        assert stock.logo == 'logo.svg'
        assert stock.sector == 'development'

    def test___str__(self):
        stock = Stock.objects.create(
            code='ABC1',
            name='Abstract Basic',
            logo='logo.svg',
            sector='development')
        assert str(stock) == 'Abstract Basic'


class TestQuoteModel:
    def test_crete_quote(self):
        stock = StockFactory()
        quote = Quote.objects.create(
            price=5.60,
            stock=stock
        )

        assert quote.price == 5.60
        assert quote.stock == stock
        