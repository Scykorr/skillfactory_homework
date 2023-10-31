from bs4 import BeautifulSoup
import requests
base = 'https://ru.stackoverflow.com' # выносим базовую ссылку в отдельную переменную, она нам потом понадобится
html = requests.get(base).content # с помощью уже знакомой нам библиотеки requests получаем html код странички целиком
soup = BeautifulSoup(html, 'lxml') # создаём объект супа.
# Первый аргумент в конструкторе - это весь html код.
# Второй аргумент - сама библиотека для парсинга. В нашем случае lxml
div = soup.find('div', id='question-mini-list') # находим с помощью метода find()
# нужный нам див уточняя id
print(div) # пишем в консоль то что нашли
