import json
import re
from bs4 import BeautifulSoup
import time

with open('beijing_response', 'r', encoding='utf-8') as f:
    response_text = json.loads(f.read())


def remove_html_tags(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    soup = BeautifulSoup(text, "html.parser")
    text = ' '.join(soup.stripped_strings)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text


data_list = response_text['data']['results']

content = data_list[0]['text']


# print(content)
# print(remove_html_tags(content))

def make_beijing_string(each):
    content = each['text']
    data_str = "".join(remove_html_tags(each['title']).strip().split()) + "".join(
        remove_html_tags(content).strip().split()) + each['path'] + each['publishedAt'] + "\n"
    return data_str


title_list = []
content_list = []
path_list = []
date_list = []
for each in data_list:
    content = each['text']
    title_list.append("".join(remove_html_tags(each['title']).strip().split()))
    content_list.append("".join(
        remove_html_tags(content).strip().split()))
    path_list.append(each['path'])
    date_list.append(each['publishedAt'])

# print(title_list)
print(content_list)
# print(path_list)
# print(date_list)
