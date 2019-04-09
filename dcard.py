import requests #引入函式庫
from bs4 import BeautifulSoup
import re
url = 'https://www.dcard.tw/f'
resp = requests.get(url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')
dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))
print('Dcard 熱門前十文章標題：')
for index, item in enumerate(dcard_title[:10]):
    print("{0:2d}. {1}".format(index + 1, item.text.strip()))
