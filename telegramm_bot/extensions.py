import json
import requests
from config import currencies
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class APIException(Exception):
    """
    Класс исключений ошибок пользователя.

    ...

    """
    pass


class CurrencyConverter:
    """
    Класс конвертера валют.

    ...


    Methods
    -------
    @staticmethod
    get_price(base: str, quote: str, amount: str) -> float:
        Метод, конвертирующий валюту.
    """

    @staticmethod
    def get_price(base: str, quote: str, amount: str) -> float:
        """
        Метод, конвертирующий валюту.

        Parameters
        ----------
            quote : str
                валюта из которой конвертируем
            base : str
                валюта в которую конвертируем
            amount : int
                количество конвертируемой валюты

        Returns
        -------
            total_quote : float
                итоговое количество конвертируемой валюты
        """
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты: {base}.')

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту: {quote}')

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество: {amount}')

        main_request = requests.get(
            f'https://v6.exchangerate-api.com/v6/{os.getenv('api_token')}/pair/{base_ticker}/{quote_ticker}')
        total_quote = float(json.loads(main_request.content)['conversion_rate'] * amount)
        return total_quote
