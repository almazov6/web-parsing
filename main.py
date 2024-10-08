import requests
import bs4


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')

article_list = soup.findAll('article', class_='tm-articles-list__item')

for article in article_list:
    link = f'https://habr.com{article.find('a', class_='tm-title__link')['href']}'
    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text, features='lxml')
    date_soup = soup.find('span', class_='tm-article-datetime-published')
    title_soup = soup.find('h1', class_='tm-title_h1')
    text_soup = soup.find('div', class_='article-formatted-body').div.p
    date = date_soup.time['datetime'][:10]
    title = title_soup.text
    if text_soup == None:
        continue
    text = text_soup.text.lower()
    for item in KEYWORDS:
        if item in text:
            print(f'{date} - {title} - {link}')