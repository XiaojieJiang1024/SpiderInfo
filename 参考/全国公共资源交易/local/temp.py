import re

from bs4 import BeautifulSoup
from curl_cffi import requests
from requests import Response

def remove_html_tags(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    soup = BeautifulSoup(text, "html.parser")
    text = ' '.join(soup.stripped_strings)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


import re


def process_government_tender_text(text):
    """
    将政府采购公告文本按章节标题切分成自然段。

    参数:
        text (str): 原始文本内容

    返回:
        str: 格式化后的内容，包含清晰的章节和换行，适合写入 txt 文件
    """
    # 正则匹配类似“一、项目基本情况”这样的标题
    section_pattern = re.compile(r'([一二三四五六七八九十]+)、([^\n]+)')
    sections = section_pattern.split(text)

    formatted_output = []
    i = 1  # 跳过第一个匹配项（空）

    while i < len(sections) - 1:
        title = sections[i] + "、" + sections[i + 1].strip()
        content_start = text.find(title) + len(title)

        # 查找下一个标题位置
        next_section_match = section_pattern.search(text[content_start:])
        if next_section_match:
            content_end = content_start + next_section_match.start()
            content = text[content_start:content_end].strip()
        else:
            content = text[content_start:].strip()

        # 添加格式化段落，每段之间用两个换行符隔开
        formatted_output.append(f"=== {title.strip()} ===\n")
        formatted_output.append(f"{content}\n\n")

        i += 2

    return ''.join(formatted_output)




cookies = {
    'insert_cookie': '91349450',
    'JSESSIONID': '7bbec5a342ec43c49aebae743c51',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.ggzy.gov.cn/information/html/a/420000/0201/202506/14/0042dcc94f803f0a4057adcb101c414a2635.shtml',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

url = 'https://www.ggzy.gov.cn/information/html/b/420000/0201/202506/14/0042dcc94f803f0a4057adcb101c414a2635.shtml'

response: Response = requests.get(url, headers=headers, cookies=cookies, verify=False)

res = remove_html_tags(response.text)
# print(res)


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


improved_text_segmenter(res, "henan123.txt")