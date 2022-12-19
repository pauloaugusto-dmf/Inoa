import requests

from typing import List, Dict

BASE_URL = 'https://brapi.dev/api/'


class StocksInfo():
    def __init__(self) -> None:
        self.stocks = self.get()

    def get(self):
        return requests.get(BASE_URL + 'quote/list')

    def formatted(self, stock: Dict) -> Dict:
        stock_formatted = {
            'code': stock['stock'],
            'name': stock['name'],
            'logo': stock['logo'],
            'sector': stock['sector']
        }
        return stock_formatted

    def to_json(self):
        return self.stocks.json()['stocks']

    def __iter__(self) -> List[Dict]:
        return iter(map(self.formatted, self.to_json()))

    def __str__(self) -> str:
        return self.stocks.text

class StocksAvailables():
    def __init__(self) -> None:
        self.stocks_availables = self.get()

    def get(self):
        return requests.get(BASE_URL + 'available')

    def to_json(self):
        return self.stocks_availables.json()['stocks']

    def __iter__(self) -> List:
        return iter(self.stocks_availables.json()['stocks'])

    def __str__(self) -> str:
        return self.stocks_availables.text

class Quotes():
    def __init__(self, stocks) -> None:
        self.quotes_formatted = self.get(stocks)

    def get(self, stocks: List):
        query = ""
        for stock in stocks: query += stock + "%2C"
        return requests.get(BASE_URL + 'quote' + f'/{query[:-3]}')

    def formatted(self, stock: Dict) -> Dict:
        try:
            quotes_formatted = {
                'code': stock['symbol'],
                'price': stock['regularMarketPrice']
            }
            return quotes_formatted
        except:
            ...

    def to_json(self):
        return self.quotes_formatted.json()['results']

    def __iter__(self) -> List[Dict]:
        return iter(map(self.formatted, self.to_json()))

    def __str__(self) -> str:
        return self.quotes_formatted.text

