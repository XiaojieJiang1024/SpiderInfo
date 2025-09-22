import requests

cookies = {
    'HMF_CI': 'ee3a1bf94fc7b7e034611be0a5ab28292b1423b77fa306de9df2aae7f42c143849b0b57275c59713bbc19e88b2733d8b3eb1966368ab564fda756de0548dc7521b',
    'Hm_lvt_9459d8c503dd3c37b526898ff5aacadd': '1749396223,1749439943',
    'HMACCOUNT': 'BF2A4C098F80CDB1',
    'Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5': '1749396158,1749440069',
    'Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5': '1749440069',
    'HMACCOUNT': 'BF2A4C098F80CDB1',
    'JSESSIONID': 'LL9Szkv4xNV5Rzf6BxBuNsgcMmZsFbhzrftGsyOAQGRXt9C9_Hfm!-61981476',
    'HMY_JC': 'b394258e2a14d35bac149dbcc77fba6620d2f6ab6a9b422e6126ed2f8ec8f422a5,',
    'HBB_HC': '99f4836c9e21dcbaba962d9ff9fdedb6cd4e3484d215b037b8ffc149e8747e620799478e6727f24cd7f858dc2acb3a681b',
    'Hm_lpvt_9459d8c503dd3c37b526898ff5aacadd': '1749440950',
    'CSH_DF': 'amcnglxYSTt2huiKQ9GILqaNPvcQxVOIX6RhcfG/s6QVDH011f15kBH6lYXeaD2sW2',
    'CSH_UF': '0fe6feb54289f4c67027ec06cc2131f8',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index=1&bidSort=&buyerName=&projectId=&pinMu=&bidType=&dbselect=bidx&kw=%E6%B2%B3%E5%8D%97&start_time=2025%3A06%3A02&end_time=2025%3A06%3A09&timeType=2&displayZone=&zoneId=&pppStatus=0&agentName=',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'HMF_CI=ee3a1bf94fc7b7e034611be0a5ab28292b1423b77fa306de9df2aae7f42c143849b0b57275c59713bbc19e88b2733d8b3eb1966368ab564fda756de0548dc7521b; Hm_lvt_9459d8c503dd3c37b526898ff5aacadd=1749396223,1749439943; HMACCOUNT=BF2A4C098F80CDB1; Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1749396158,1749440069; Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1749440069; HMACCOUNT=BF2A4C098F80CDB1; JSESSIONID=LL9Szkv4xNV5Rzf6BxBuNsgcMmZsFbhzrftGsyOAQGRXt9C9_Hfm!-61981476; HMY_JC=b394258e2a14d35bac149dbcc77fba6620d2f6ab6a9b422e6126ed2f8ec8f422a5,; HBB_HC=99f4836c9e21dcbaba962d9ff9fdedb6cd4e3484d215b037b8ffc149e8747e620799478e6727f24cd7f858dc2acb3a681b; Hm_lpvt_9459d8c503dd3c37b526898ff5aacadd=1749440950; CSH_DF=amcnglxYSTt2huiKQ9GILqaNPvcQxVOIX6RhcfG/s6QVDH011f15kBH6lYXeaD2sW2; CSH_UF=0fe6feb54289f4c67027ec06cc2131f8',
}

params = {
    'searchtype': '1',
    'page_index': '1',
    'bidSort': '',
    'buyerName': '',
    'projectId': '',
    'pinMu': '',
    'bidType': '',
    'dbselect': 'bidx',
    'kw': '河南',
    'start_time': '2025:06:02',
    'end_time': '2025:06:09',
    'timeType': '2',
    'displayZone': '',
    'zoneId': '',
    'pppStatus': '0',
    'agentName': '',
}

response = requests.get('https://search.ccgp.gov.cn/bxsearch', params=params, cookies=cookies, headers=headers)
print(response.text)