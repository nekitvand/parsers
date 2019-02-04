from bs4 import BeautifulSoup
import requests


def get_html(url):
    """Получает HTMTL код страницы"""
    r = requests.get(url)
    return r.text

def get_data(html):
    """Парсит данные со страницы"""
    parse = BeautifulSoup(html , 'lxml')
    get_text = parse.find('div',id='content').find('header', 'entry-header').text
    return get_text

def main():
    """Вызывает функции в нужном порядке """
    url = 'https://pythonworld.ru/'
    print(get_data(get_html(url)))



if __name__ == '__main__':
    main()