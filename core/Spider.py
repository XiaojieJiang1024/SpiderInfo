import os

import requests
from write_file import WriteFile
from .. import settings

write_file = WriteFile.WriteInfo()


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

    def __init__(self, url, file_name, file_path=settings.default_dir, multi_folders=None):
        self.url = url
        self.file_name = file_name
        self.file_path = file_path
        self.multi_folders = multi_folders

    def single_download(self):
        res = requests.get(self.url, headers=self.headers, cookies=self.cookies)
        print(res.text)

    def multi_download(self):
        save_dir = os.path.join(settings.default_dir, self.multi_folders)
        print(save_dir)

    def check_choices(self):
        start_list = []
        for name in self.file_name:
            if not settings.support_dict[name]:
                raise ValueError("不支持的类型")
            start_list.append(settings.support_dict[name])

        for operation in start_list:
            getattr(write_file, operation)

    def download(self):
        self.check_choices()
        if self.multi_folders:
            self.single_download()
        self.multi_download()
