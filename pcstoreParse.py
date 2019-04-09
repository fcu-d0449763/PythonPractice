import requests
import base64
from bs4 import BeautifulSoup
import re

headers = {
    'authority': 'www.pcstore.com.tw',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'origin': 'https://www.pcstore.com.tw',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'referer': 'https://www.pcstore.com.tw/adm/psearch.htm?store_k_word=YWE=^&slt_k_option=1',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,zh-CN;q=0.7',
    'cookie': 'brwsckidsn=CObRlRVexMUJJCSMkqJoj1OiHMRKTu1Hnb; c_c=0; ShowPageStyleByUser=a^%^3A1^%^3A^%^7Bs^%^3A9^%^3A^%^22showstyle^%^22^%^3Bs^%^3A9^%^3A^%^22GraphWord^%^22^%^3B^%^7D; pagecountBycookie=20',
}


data = {
  'type_code': '^',
  'send_keyword': '^',
  'slt_k_option': '1^',
  'store_k_word': 'vvvv^',
  'store_k_word2': 'aa^',
  'slt_p_range_s': '^',
  'slt_p_range_e': '^',
  'slt_k_option3': '1^',
  'store_k_word3': 'vvvv^',
  'page_count': '20'
}

while 1:
    keyword = input("輸入關鍵字(輸入0停止程式)：")
    if keyword =='0':
        break
    keyword64 = base64.b64encode(bytes(keyword, 'utf-8'))
    params = (
        ('store_k_word', keyword64),
        ('slt_k_option', '1'),
    )
    response = requests.post('https://www.pcstore.com.tw/adm/psearch.htm', headers=headers, params=params, data=data)
    response.encoding = 'big5-hkscs'
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all(class_=re.compile("pic2t_bg"))
    for i in titles:
        print(i.text)


