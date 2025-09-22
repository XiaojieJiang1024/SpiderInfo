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
bag_name = page.find('h1', class_='s-title').text
publish_time = page.find('div', class_='s-date').text
price = page.find('p', class_='Normal', style='text-align:right;').text
print(publish_time)
print(bag_name)
print(price)
