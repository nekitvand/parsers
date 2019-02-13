from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    """Получает HTMTL код страницы"""
    r = requests.get(url)
    return r.text


def refined(s):
    # 792 total ratings
    r = s.split(' ')[0]
    return r.replace(u'\xa0', '')


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f,delimiter=',')

        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))

def get_data(html):
    """Парсит данные со страницы"""
    parse = BeautifulSoup(html , 'lxml')
    popular = parse.find_all('section')[1]
    plagins = popular.find_all('article')

    for popular_plagin in plagins:
        name = popular_plagin.find('h2').text
        url = popular_plagin.find('h2').find('a').get('href')

        r = popular_plagin.find('span', class_='rating-count').find('a').text
        rating = refined(r)

        data = {'name': name,
                'url': url,
                'reviews': rating}


        write_csv(data)
        # print(data)


def main():
    """Вызывает функции в нужном порядке """
    url = 'https://ru.wordpress.org/plugins/'
    get_data(get_html(url))



if __name__ == '__main__':
    main()