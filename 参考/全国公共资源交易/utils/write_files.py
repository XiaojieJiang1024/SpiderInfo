import re
from curl_cffi import requests
from requests import Response
from bs4 import BeautifulSoup
import os
import pandas as pd

dir_name = 'files'

if not os.path.exists(dir_name):
    os.makedirs(dir_name)


def remove_html_tags(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    soup = BeautifulSoup(text, "html.parser")
    text = ' '.join(soup.stripped_strings)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def improved_text_segmenter(content, output_file):


    section_markers = ['一、', '二、', '三、', '四、', '五、', '六、', '七、', '八、', '九、', '十、']

    # 先按特殊标记分割
    segments = []
    start = 0
    for marker in section_markers:
        idx = content.find(marker, start)
        if idx != -1:
            segments.append(content[start:idx])
            start = idx
    segments.append(content[start:])  # 添加最后一段

    # 对每个大段再按项目编号细分
    refined_segments = []
    for segment in segments:
        # 处理带数字编号的段落（如1、2、3）
        sub_segments = []
        lines = segment.split('\n')
        current_segment = []

        for line in lines:
            stripped = line.strip()
            # 检测项目编号行（如"1、"开头）
            if stripped and (stripped[0].isdigit() and stripped[1] in ['、', '.']) or \
                    (len(stripped) > 2 and stripped[0] == '(' and stripped[1].isdigit()):
                if current_segment:
                    sub_segments.append('\n'.join(current_segment))
                    current_segment = []
            current_segment.append(line)

        if current_segment:
            sub_segments.append('\n'.join(current_segment))

        refined_segments.extend(sub_segments)

    # 写入文件，确保段落间有空行
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, segment in enumerate(refined_segments):
            f.write(segment.strip())
            if i < len(refined_segments) - 1:
                f.write('\n\n')

cookies = {
    'insert_cookie': '97324480',
    'JSESSIONID': 'f3f056141555e1c54acb99ebc617',
    'insert_cookie': '97324480',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.ggzy.gov.cn/information/html/a/510000/0201/202506/25/0051ef644deaf2154aa49ebeebcc00b38e4e.shtml',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'insert_cookie=97324480; JSESSIONID=f3f056141555e1c54acb99ebc617; insert_cookie=97324480',
}


def write_text(title, url):
    response: Response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
        verify=False
    )
    res = remove_html_tags(response.text)
    improved_text_segmenter(res, "files/{}.txt".format(title))
    # with open("files/{}.txt".format(title), "w", encoding="utf-8") as f:
    #     f.write(remove_html_tags(response.text))
    # print(remove_html_tags())


def write_excel(province, title_list, url_list, time_list):
    data = {
        "标题": title_list,
        "链接": url_list,
        "时间": time_list,
    }

    # 转换为 DataFrame
    df = pd.DataFrame(data)

    # 导出到 Excel（不保存索引）
    df.to_excel("files/{}.xlsx".format(province), index=False)

    print("Excel 文件已生成！")
