import requests
from bs4 import BeautifulSoup


china_cookies = {
    'Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5': '1749396158',
    'Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5': '1749396158',
    'HMACCOUNT': 'BF2A4C098F80CDB1',
    'JSESSIONID': '-ktQI_L5W_z0KijABuFUPDWCwXIR9EsNcuOtvAqdN_rIfuSGMV7r!485428781',
    'HMF_CI': 'ee3a1bf94fc7b7e034611be0a5ab28292b1423b77fa306de9df2aae7f42c143849b0b57275c59713bbc19e88b2733d8b3eb1966368ab564fda756de0548dc7521b',
    'Hm_lvt_9459d8c503dd3c37b526898ff5aacadd': '1749396223',
    'Hm_lpvt_9459d8c503dd3c37b526898ff5aacadd': '1749396223',
}

china_headers = {
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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1749396158; Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1749396158; HMACCOUNT=BF2A4C098F80CDB1; JSESSIONID=-ktQI_L5W_z0KijABuFUPDWCwXIR9EsNcuOtvAqdN_rIfuSGMV7r!485428781; HMF_CI=ee3a1bf94fc7b7e034611be0a5ab28292b1423b77fa306de9df2aae7f42c143849b0b57275c59713bbc19e88b2733d8b3eb1966368ab564fda756de0548dc7521b; Hm_lvt_9459d8c503dd3c37b526898ff5aacadd=1749396223; Hm_lpvt_9459d8c503dd3c37b526898ff5aacadd=1749396223',
}

china_params = {
    'searchtype': '1',
    'page_index': '1',
    'start_time': '',
    'end_time': '',
    'timeType': '2',
    'searchparam': '',
    'searchchannel': '0',
    'dbselect': 'bidx',
    'kw': '招标',
    'bidSort': '0',
    'pinMu': '0',
    'bidType': '0',
    'buyerName': '',
    'projectId': '',
    'displayZone': '',
    'zoneId': '',
    'agentName': '',
}

response = requests.get('https://search.ccgp.gov.cn/bxsearch', params=china_params, cookies=china_cookies, headers=china_headers)
print(response.text)
# page = BeautifulSoup(response.text, 'html.parser')
# ul = page.find('ul', attrs={'class': 'vT-srch-result-list-bid'})
# print(ul)
# li_list = ul.find_all('li')
# for li in li_list:
#     href = li.find('a')['href']
#     title = li.find('a')
#     publish_time = li.find('span')
#     print(href, title, publish_time)