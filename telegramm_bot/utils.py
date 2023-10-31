import json
import requests
from config import currencies
from pprint import pprint


class ConversionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}')

        main_request = requests.get(f'https://openexchangerates.org/api/latest.json?app_id=a03fd78882a74dd48de13b9ec3f26e72'
                                    f'&base={base_ticker}&symbols={quote_ticker}')
        pprint(main_request)
        print(type(main_request))
        total_quote = float(json.loads(main_request.content)['rates'][currencies[quote]]) * amount
        return total_quote