import telebot
from config import telegram_token, currencies
from extensions import APIException, CryptoConverter


def main():
    bot = telebot.TeleBot(telegram_token)

    @bot.message_handler(commands=['start', 'help'])
    def handle_start_help(message: telebot.types.Message):
        text = ('Данные вводятся в формате:\n<1>\' \'<2>\' \'<3>'
                '\n"1" - имя валюты, цену которой хотите узнать'
                '\n"2" - имя валюты, в которой надо узнать цену первой валюты'
                '\n"3" - количество первой валюты'
                '\n\' \' - пробел\n'
                '\nСписок доступных команд: /commands')
        bot.reply_to(message, text)

    @bot.message_handler(commands=['commands'])
    def handle_check_commands(message: telebot.types.Message):
        text = ('Доступные комманды:\n'
                '/values - список всех доступных валют')
        bot.reply_to(message, text)

    @bot.message_handler(commands=['values'])
    def handle_check_currencies(message: telebot.types.Message):
        output_text = 'Доступные валюты:'
        for key in currencies.keys():
            output_text = '\n'.join((output_text, key,))
        bot.reply_to(message, output_text)

    @bot.message_handler(content_types=['text', ])
    def covert_currencies(message: telebot.types.Message):
        try:
            values = message.text.split(' ')

            if len(values) != 3:
                raise APIException('Неверное количество параметров!')

            base, quote, amount = values
            total_base = CryptoConverter.get_price(base, quote, amount)
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
