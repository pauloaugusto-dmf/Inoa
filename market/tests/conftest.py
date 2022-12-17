import pytest

from .factories import StockFactory, QuoteFactory

@pytest.fixture
def stock():
    return StockFactory()

@pytest.fixture
def quote():
    return QuoteFactory()