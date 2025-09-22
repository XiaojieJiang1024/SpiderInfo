import bs4
import requests

cookies = {
    # 'insert_cookieXJDDMZ': '75821406',
    # 'clientlanguage': 'zh_CN',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.bidding.csg.cn/zbgg/index_3.jhtml',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'insert_cookieXJDDMZ=75821406; clientlanguage=zh_CN',
}

response = requests.get('https://www.bidding.csg.cn/zbgg/1200403673.jhtml', cookies=cookies, headers=headers)
page = bs4.BeautifulSoup(response.text, 'html.parser')

table = page.find('table', attrs={'cellspacing': '0'})
body = table.find_all('tr')
# print(body)
line = ""
res = ""
for row in body[0].find_all('span'):
    line = line + row.text + " "
for row in body[1].find_all('span'):
    res = res + row.text + " "
print(line)
print(res)
