import requests
import bs4

cookies = {
    'insert_cookieXJDDMZ': '75821406',
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
    # 'Cookie': 'insert_cookieXJDDMZ=75821406',
}

response = requests.get('https://www.bidding.csg.cn/zbgg/index_2.jhtml', cookies=cookies, headers=headers)
page = bs4.BeautifulSoup(response.text, 'html.parser')
table = page.find("div", attrs={"class": "List2"}).find_all("li")
for link in table:
    title_tag = link.find('a', href=True, target='_blank')
    title = title_tag.get_text(strip=True)
    new_link = title_tag['href']
    unit_tag = link.find('a', class_='Blue')
    unit = unit_tag.get_text(strip=True) if unit_tag else '未知单位'
    print(new_link, unit)
    print(":::")
