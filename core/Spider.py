import os

import requests
from write_file import WriteFile
from .. import settings

from clear_data.Filter import FilterData


class MyWriteInfo(WriteFile):
    pass


class MyFilterData(FilterData):
    pass


write_file = MyWriteInfo
filter_data = MyFilterData


class SpiderInfo:
    cookies = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    }
    params = {}

    def __init__(self, url, file_name, file_type, is_multi=false, file_path=settings.default_dir):
        self.url = url
        self.file_name = file_name
        self.file_path = file_path
        self.file_type = file_type
        self.is_multi = is_multi
        self.download()

    def check_choices(self, res):
        start_list = []
        for name in self.file_name:
            if not settings.support_dict[name]:
                raise ValueError("不支持的类型")
            start_list.append(settings.support_dict[name])
        obj = write_flie(res)
        for operation in start_list:
            getattr(write_file, operation)

    def download(self):
        if not is_multi:
            res = self.single_download()
        else:
            res = self.multi_download()

        self.check_choices(res)

def single_download(self):
    res = requests.get(self.url, headers=self.headers, cookies=self.cookies)
    print(res.text)


# 这个主要是递归下载，比方说有好几个章节，每个章节都对应了内容。
def multi_download(self):
    save_dir = os.path.join(settings.default_dir, self.multi_folders)
    print(save_dir)
