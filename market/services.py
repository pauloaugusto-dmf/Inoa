from .request import StocksInfo, Quotes
from .models import Stock, Quote


def stock_register():
    stocks = StocksInfo()
    for stock in stocks:
        Stock.objects.create(
            code=stock['code'],
            name=stock['name'],
            logo=stock['logo'],
            sector=stock['sector'])
    return stocks

def quote_register():
    stocks = list(Stock.objects.all())
    stocks = list(map(lambda stock:stock.code, stocks))
    quotes = Quotes(stocks)
    for quote in quotes:
        stock = Stock.objects.get(code=quote['code'])
        Quote.objects.create(
            price=quote['price'],
            stock=stock
        )
    return quotes
