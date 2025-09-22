import re

import bs4
import requests

cookies = {
    'insert_cookieXJDDMZ': '45380249',
    'clientlanguage': 'zh_CN',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'insert_cookieXJDDMZ=45380249; clientlanguage=zh_CN',
}

response = requests.get('https://www.bidding.csg.cn/zbgg/1200404616.jhtml', cookies=cookies, headers=headers)
page = bs4.BeautifulSoup(response.text, 'html.parser')
content = str(page.find('div', class_='s-content'))

new_content = re.sub(r'<.*?>', '', content)
the_content = re.sub(r'{.*?}', '', new_content)
css_noise_patterns = [
    'bodyul', 'ul', 'ol', 'Normal', 'Heading-1', 'Heading-2', 'Title', 'Body-Text',
    'Default-Paragraph-Font', 'Strong', 'Table-Grid', 'List-Paragraph', 'No-List',
    'Normal-Table', 'lang', 'mso-', 'font-family', 'font-size', 'color', 'margin',
    'text-indent', 'border', 'page-break', 'line-height', 'text-align', '-Table',
    'No-List'
]

# 构造正则：匹配这些单词（单独出现的）
# 使用 \b 表示单词边界，避免误删正文中的词
noise_pattern = r'\b(?:' + '|'.join(re.escape(word) for word in css_noise_patterns) + r'(?:-\w+)*)\b'

# 先移除明显的 CSS 噪声
text = re.sub(noise_pattern, '', the_content)
cleaned_text = re.sub(r',\s*\.*No-List', '', text)
print(cleaned_text)
# print(content)
# def remove_html_tags(text):
#     text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
#     soup = bs4.BeautifulSoup(text, "html.parser")
#     text = ' '.join(soup.stripped_strings)
#     text = re.sub(r'&[a-z]+;', ' ', text)
#     text = re.sub(r'\s+', ' ', text).strip()
#
#     return text


# new_content = remove_html_tags(content)
# print(new_content)
