from bs4 import BeautifulSoup
import urllib.request


def get_head(url):
    html_doc = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    return str(soup.find_all('td'))


url = 'http://noblit.ru/Laureates'
result = iter(get_head(url).split('\n')[1:])
laureates = {}
for name, year, _ in zip(result, result, result):
    name = name.replace('<', '*').replace('>', '*').split('*')[2]
    year = year.split()[0].strip()
    laureates[name] = year

name = input('Имя: ')
if name in laureates:
    print(f'лауреат - {name}, год вручения - {laureates[name]}')
else:
    print('Нет совпадений')