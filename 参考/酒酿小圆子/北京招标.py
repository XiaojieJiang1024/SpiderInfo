import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'http://www.ccgp-beijing.gov.cn',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}


json_data = {
    'site': 'A002',
    'indexes': None,
    'keywords': '+"广州"',
    'fields': None,
    'range': None,
    'orderBy': 'TIME',
    'current': 1,
    'size': 50,
    'requrl': 'www.ccgp-beijing.gov.cn',
    'page': 1,
}

response = requests.post('http://www.ccgp-beijing.gov.cn/api/search/query', headers=headers, json=json_data, verify=False)

print(response.text)