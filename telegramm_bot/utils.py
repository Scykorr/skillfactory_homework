import json
import requests
from config import currencies


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

        main_request = requests.get(f'https://min-api.cryptocompare.com/data/price?'
                                    f'fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = float(json.loads(main_request.content)[currencies[base]]) * amount
        return total_base