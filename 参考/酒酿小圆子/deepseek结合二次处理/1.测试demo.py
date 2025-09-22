from openai import OpenAI
import requests


api_key = "sk-5829b79fa9864a28aa91d735798d5895"
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

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你现在帮我处理爬虫爬到的数据，获取内容的标题，内容，简介，时间这些内容。统一格式返回。 必须全部处理完！！！"},
        {"role": "user", "content": response.text},
    ],
    stream=False
)

print(response.choices[0].message.content)
