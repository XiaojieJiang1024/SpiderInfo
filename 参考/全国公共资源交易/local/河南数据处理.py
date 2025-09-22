import ast
import re

from bs4 import BeautifulSoup

with open('he_nan', 'r', encoding='utf-8') as f:
    response_text = ast.literal_eval(f.read())


def clean_text(text):
    res = re.sub(r'<[^>]+>', '', text)
    return res


data_list = response_text['data']
# print(len(data_list))
# print(data_list[0])
# print(data_list[0]['title'])
# print(data_list[0]['timeShow'])
# print(data_list[0]['url'])
# print(clean_text(data_list[0]['titleShow']))

url_list = []
title_list = []
for data in data_list:
    title = data['title']
    timeShow = data['timeShow']
    url = data['url']
    url_list.append(url)
    title_list.append(title)
    print(title, timeShow, url)
# print(url_list)
print(title_list)