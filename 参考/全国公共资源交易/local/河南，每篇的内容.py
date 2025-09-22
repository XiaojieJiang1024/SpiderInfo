import re
from curl_cffi import requests
from requests import Response

from bs4 import BeautifulSoup


def remove_html_tags(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    soup = BeautifulSoup(text, "html.parser")
    text = ' '.join(soup.stripped_strings)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text


cookies = {
    'insert_cookie': '67313298',
    'JSESSIONID': 'd126ef46b061f51c1c9e1911b414',
    'insert_cookie': '67313298',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.ggzy.gov.cn/information/html/a/410000/0202/202506/10/0041cd2dfccff7e049fa8b11c8daaad7b28d.shtml',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'insert_cookie=67313298; JSESSIONID=d126ef46b061f51c1c9e1911b414; insert_cookie=67313298',
}

url_list = [
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202506/16/0041c8e0f6578c5040f68a9c2608efca5607.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202506/13/0041ae96be9ce67145949cf26f5424d4a844.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0201/202506/13/0041753721b075fa466e8ee7f0543b2a84b9.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0201/202506/11/0041f218a5def0bb4d89b0d5f9cd63fac6c8.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0201/202506/11/00418ed2e76ec92342c095bd6916c3c841fb.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202506/10/0041cd2dfccff7e049fa8b11c8daaad7b28d.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0201/202506/09/00417a05183b6e8e449a9510645eebc095c1.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202506/06/0041589b8e91dae64f629a7940afdbe150a0.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0201/202506/06/00416a8b3f2982354dbdae1f1c1d51e77c2a.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0201/202506/05/004142684f6fe9374f33a7b2a81b6faa1784.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202506/05/00414db12e52c9914b709d50058e05e459d5.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0203/202506/04/0041466614b886a346a4bf71af48431f3934.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202506/04/00415d16e192e01c4d239517ccf62fbbc14e.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202506/03/00417bbc5fbb6bef4ca1bddb613733f84189.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0201/202505/31/0041b69ca30b5aaa457ea2e07d4d57cddebc.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0201/202505/30/00414dee4352e4ea4477acf093574986c611.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202505/30/0041b75db7c13bab4ab0b1dbbf84c53c7338.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202505/30/0041786a4f9446d44fff8fa00f31b91211a5.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202505/30/0041ddf02701b7e340f28a28a1a8f225c616.shtml',
    'http://www.ggzy.gov.cn/information/html/a/410000/0202/202505/30/00413d6c5d18601a411eb58b6838eb266184.shtml']
title_list = ['洛阳市偃师区教育体育局偃师区公办中小学校食堂食材大宗采购（含数字化供餐平台）项目-中标公告',
              '郑州市公安局金水分局购买餐厅食材供应服务项目-中标公告',
              '汝阳县消防救援大队2025年-2026年食堂食材采购项目-竞争性磋商公告',
              '鹤壁工业中专食堂大宗食材采购项目竞争性磋商公告',
              '鹤壁市第一中学食堂大宗食材采购及配送服务项目-竞争性磋商公告',
              '洛阳市政务保障中心部分食堂食材配送服务项目-成交公告',
              '开封市祥符区消防救援大队食材配送供应商采购项目-招标[采购]公告',
              '夏邑县教育体育局全县校园餐大宗食材集中配送服务项目结果公告',
              '洛阳市公安局洛龙分局食堂食材采购项目-竞争性磋商公告',
              '商丘市睢阳区教育体育局睢阳区校园餐大宗食材供应项目招标公告',
              '郑州市儿童福利院（郑州市儿童福利院特殊教育学校）儿童餐厅食材采购项目-中标公告',
              '平顶山市夕阳红老年公寓食材供应商服务项目', '获嘉县大宗食材集采集配运营商项目中标公示',
              '【平公资采2025392号】平顶山市夕阳红老年公寓食材供应商服务项目-中标公告',
              '卫辉市校园阳光智慧监管平台及食材供应链供应管理服务项目',
              '洛阳市政务保障中心部分食堂食材配送服务项目-竞争性磋商公告',
              '南阳高新技术产业开发区综合办公室管委会机关餐厅食材采购项目-成交公告',
              '新乡市公安局局直单位食堂食材集中采购项目-中标公告',
              '中华人民共和国第三届全国职业技能大赛郑州航空港经济综合实验区梅河芳邻选手村餐饮及食材供应服务项目中标结果公告',
              '周口市公安局民警餐厅食材配送项目-中标公告']
for title, url in zip(title_list, url_list):
    response: Response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
        verify=False
    )
    with open("files/{}.txt".format(title), "w", encoding="utf-8") as f:
        f.write(remove_html_tags(response.text))
    # print(remove_html_tags())
