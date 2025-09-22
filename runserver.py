import os
from core.info_requests.Spider import SpiderInfo
from settings import default_dir

print(default_dir)
if not os.path.exists(default_dir):
    os.makedirs(default_dir)


class SpiderApi(SpiderInfo):
    def call_method(self):
        pass