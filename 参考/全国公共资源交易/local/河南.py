import requests

cookies = {
    'JSESSIONID': 'd20434beb5c7ff8c12db7c896f4c',
    'JSESSIONID': 'd20434beb5c7ff8c12db7c896f4c',
    'insert_cookie': '61459989',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://deal.ggzy.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://deal.ggzy.gov.cn/ds/deal/dealList.jsp?HEADER_DEAL_TYPE=02',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'JSESSIONID=d20434beb5c7ff8c12db7c896f4c; JSESSIONID=d20434beb5c7ff8c12db7c896f4c; insert_cookie=61459989',
}

data = {
    'TIMEBEGIN_SHOW': '2025-06-08',
    'TIMEEND_SHOW': '2025-06-17',
    'TIMEBEGIN': '2025-06-08',
    'TIMEEND': '2025-06-17',
    'SOURCE_TYPE': '1',
    'DEAL_TIME': '04',
    'DEAL_CLASSIFY': '02',
    'DEAL_STAGE': '0200',
    'DEAL_PROVINCE': '410000',
    'DEAL_CITY': '0',
    'DEAL_PLATFORM': '0',
    'BID_PLATFORM': '0',
    'DEAL_TRADE': '0',
    'isShowAll': '1',
    'PAGENUMBER': '1',
    'FINDTXT': '食材',
}

response = requests.post('https://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp', cookies=cookies, headers=headers, data=data)
print(response.json())