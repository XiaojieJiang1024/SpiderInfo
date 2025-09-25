import os
import requests
from core.Spider import SpiderInfo
from settings import default_dir

print(default_dir)
if not os.path.exists(default_dir):
    os.makedirs(default_dir)


# 这里可以自定制参数，比如cookie，params
class SpiderApi(SpiderInfo):
    # 我也不知道使用者到底要啥玩意，所有这里自定义
    def single_download(self):
        res = requests.get(self.url, headers=self.headers, cookies=self.cookies)
        print(res.text)


url = "http://www.ccgp-beijing.gov.cn/api/search/query"
file_name = "北京招标"

SpiderApi(url, file_name, file_type="text")
