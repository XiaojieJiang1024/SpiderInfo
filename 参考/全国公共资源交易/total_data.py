import requests
import os
from datetime import datetime
from utils.write_files import write_text, write_excel
from utils.per_page import get_per_page
from utils import local_settings

dir_name = 'files'

if not os.path.exists(dir_name):
    os.makedirs(dir_name)

now = datetime.now()
first_day = datetime(year=now.year, month=now.month, day=1)

keyword = input("输入关键词:")
province = input("输入省份:")
part_num = local_settings.province_dict.get(province)

cookies = {
    'JSESSIONID': '7c3524ad1ab4eb0ef34ea4a69189',
    'JSESSIONID': '7c3524ad1ab4eb0ef34ea4a69189',
    'insert_cookie': '24491169',
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
    # 'Cookie': 'JSESSIONID=7c3524ad1ab4eb0ef34ea4a69189; JSESSIONID=7c3524ad1ab4eb0ef34ea4a69189; insert_cookie=24491169',
}

data = {
    'TIMEBEGIN_SHOW': first_day.strftime("%Y-%m-%d"),
    'TIMEEND_SHOW': now.strftime("%Y-%m-%d"),
    'TIMEBEGIN': first_day.strftime("%Y-%m-%d"),
    'TIMEEND': now.strftime("%Y-%m-%d"),
    'SOURCE_TYPE': '1',
    'DEAL_TIME': '04',
    'DEAL_CLASSIFY': '02',
    'DEAL_STAGE': '0201',
    'DEAL_PROVINCE': part_num,
    'DEAL_CITY': '0',
    'DEAL_PLATFORM': '0',
    'BID_PLATFORM': '0',
    'DEAL_TRADE': '0',
    'isShowAll': '1',
    'PAGENUMBER': '1',
    'FINDTXT': keyword,
}

response = requests.post('https://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp', cookies=cookies, headers=headers,
                         data=data)
# print(response.json())
# print(type(response.json()))

total_page = response.json().get('ttlpage')
print(total_page)
title_list = []
url_list = []
time_list = []

for num in range(1, int(total_page) + 1):
    print("开始采集第{}页".format(num))
    data_list = get_per_page(keyword, part_num, num).get('data')
    for i in range(len(data_list)):
        title = data_list[i]['title']
        url = data_list[i]['url']
        title_list.append(title)
        url_list.append(url)
        time_list.append(data_list[i]['timeShow'])
        real_url = url.replace('/a/', '/b/')
        write_text(title, real_url)

write_excel(province + keyword, title_list, url_list, time_list)


