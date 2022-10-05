"""
Написать приложение или функцию, которые собирают основные новости с сайта на выбор lenta.ru, yandex-новости. Для парсинга использовать XPath.
Структура данных в виде словаря должна содержать:
- *название источника;
- наименование новости;
- ссылку на новость;
- дата публикации.
"""

from pymongo import MongoClient
from pprint import pprint
from lesson2.lenta_ru import LentaRuParser
from lesson2.yandex_ru import YandexRuParser


client = MongoClient('127.0.0.1', 27017)
db = client['news']

news_result = LentaRuParser().parse()
news_result += YandexRuParser().parse()

pprint(news_result)
