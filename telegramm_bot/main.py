import telebot
from config import currencies
from extensions import APIException, CurrencyConverter
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def main() -> None:
    """
    Основная функция работы телеграм-бота.

        Parameters:


        Returns:
            None
    """
    bot = telebot.TeleBot(os.getenv('telegram_token'))

    @bot.message_handler(commands=['start', 'help'])
    def handle_start_help(message: telebot.types.Message) -> None:
        """
        Функция, выдающая по запросу справочную информацию о работе бота.

            Parameters:
                message : telebot.types.Message
                    сообщение пользователя

            Returns:
                None
        """
        text = ('Данные вводятся в формате:\n<1>\' \'<2>\' \'<3>'
                '\n"1" - имя валюты, из какой конвертируем'
                '\n"2" - имя валюты, в которую конвертируем'
                '\n"3" - количество конвертируемой волюты'
                '\n\' \' - пробел\n'
                '\nСписок доступных команд: /commands')
        bot.reply_to(message, text)

    @bot.message_handler(commands=['commands'])
    def handle_check_commands(message: telebot.types.Message) -> None:
        """
        Функция, выдающая по запросу список команд бота.

            Parameters:
                message : telebot.types.Message
                    сообщение пользователя

            Returns:
                None
        """
        text = ('Доступные комманды:\n'
                '/values - список всех доступных валют')
        bot.reply_to(message, text)

    @bot.message_handler(commands=['values'])
    def handle_check_currencies(message: telebot.types.Message) -> None:
        """
        Функция, выдающая по запросу список доступных валют.

            Parameters:
                message : telebot.types.Message
                    сообщение пользователя

            Returns:
                None
        """
        output_text = 'Доступные валюты:'
        for key in currencies.keys():
            output_text = '\n'.join((output_text, key,))
        bot.reply_to(message, output_text)

    @bot.message_handler(content_types=['text', ])
    def covert_currencies(message: telebot.types.Message) -> None:
        """
        Функция вывода конвертированной валюты.

            Parameters:
                message : telebot.types.Message
                    сообщение пользователя

            Returns:
                None
        """
        try:
            values = message.text.split(' ')

            if len(values) != 3:
                raise APIException('Неверное количество параметров!')

            base, quote, amount = values
            base = base.lower()
            quote = quote.lower()
            total_base = CurrencyConverter.get_price(base, quote, amount)
        except APIException as e:
            bot.reply_to(message, f'Ошибка пользователя.\n{e}')
        except Exception as e:
            bot.reply_to(message, f'Не удалось обработать команду{e}')
        else:
            output_text = f'Цена {amount} {base} в {quote} - {total_base}'
            bot.send_message(message.chat.id, output_text)

    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
