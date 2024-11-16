
import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/articles/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    title = article.find('a', class_='tm-article-snippet__title-link').text
    preview = article.find('div', class_='tm-article-snippet__lead').text
    date = article.find('span', class_='tm-article-snippet__datetime-published').text
    link = article.find('a', class_='tm-article-snippet__title-link')['href']

    for keyword in KEYWORDS:
        if keyword in title.lower() or keyword in preview.lower():
            print(f'{date.strip()} - {title.strip()} - {link}')

