from pprint import pprint
import json
import requests
import telebot


def main():
    telegramm_token = '6839161996:AAGnDZ4gssYRKp4101jKjHk3NkfQOCGrbW0'

    bot = telebot.TeleBot(telegramm_token)

    # Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
    @bot.message_handler(commands=['start', 'help'])
    def handle_start_help(message: telebot.types.Message):
        bot.send_message(message.chat.id, 'Ответ')

    # Обрабатывается все документы и аудиозаписи
    @bot.message_handler(content_types=['document', 'audio'])
    def handle_docs_audio(message):
        pass

    bot.polling(none_stop=True)




if __name__ == '__main__':
    main()