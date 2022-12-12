#  -*- coding:utf-8 -*-
# Author:zhj
import requests
import bs4
# import os

html = requests.get('https://huaban.com/discovery')
html.encoding='utf-8'
print(html.text)
# txt = bs4.BeautifulSoup(html.text)
# print(txt)
