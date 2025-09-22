import requests
from utils.handle import php_unserialize

cookies = {
    'PHPSESSID': 'k2uf3t6k9ta0484fhmel1nnvce',
}

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/29.09091)',
    'Host': 'app.aiguqin.com',
    # 'Cookie': 'PHPSESSID=k2uf3t6k9ta0484fhmel1nnvce',
}

params = {
    'i': '2',
    'uniacid': '2',
    'app_ver_a': '35',
    'r': 'appApi.literature.get_list_catalogue',
    'lid': '16',
}

response = requests.get('http://app.aiguqin.com/app/ewei_shopv2_api.php', params=params, cookies=cookies, headers=headers)
print(response.json())







# total_length = len(response.json()['list'])
# total_res = response.json()['list']
# chapter = total_res['title']
# print(chapter)
# data = php_unserialize(total_res['thumb_s'])
# print(data)
# for item in data.values():
#     name, url = item['name'], item['pic']
