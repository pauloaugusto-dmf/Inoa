from .request import StocksInfo, Quotes
from .models import Stock, Quote, UserStock
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
import logging

logger = get_task_logger(__name__)

def stock_register():
    stocks = StocksInfo()
    for stock in stocks:
        Stock.objects.get_or_create(
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
        try:
            stock = Stock.objects.get(code=quote['code'])
            Quote.objects.create(
                price=quote['price'],
                stock=stock
            )
        except BaseException:
            logging.exception("An exception was thrown!")
    return quotes

def check_user_stocks():
    user_stocks = UserStock.objects.all()
    for user_stock in user_stocks:
        stock = Stock.objects.get(pk=user_stock.stock.id)
        if user_stock.min_price >= stock.quotes.last().price:
            send_buy_email(stock.name, stock.quotes.last().price, user_stock.user.email)
        if user_stock.max_price <= stock.quotes.last().price:
            send_sell_email(stock.name, stock.quotes.last().price, user_stock.user.email)
        
def send_sell_email(stock, price, user_email):
    send_mail(
        'Stock Sell',
        f'Stock {stock} reached the value of R$ {price}.\nIt\'s a good time to sell.',
        'contato@inoa.com',
        [f'{user_email}'],
        fail_silently=False,
    )

def send_buy_email(stock, price, user_email):
    send_mail(
        'Stock Buy',
        f'Stock {stock} reached the value of R$ {price}.\nIt\'s a good time to buy.',
        'contato@inoa.com',
        [f'{user_email}'],
        fail_silently=False,
    )