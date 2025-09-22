from settings import default_dir, support_dict
import pandas as pd



# 这里准备用反射搞吧，然后循环弄
class WriteInfo:
    def __init__(self, storage_path=default_dir, choices=support_dict, target_file=None):
        self.storage_path = storage_path
        self.choices = choices
        self.target_file = target_file

    def write_pdf(self):
        pass

    def write_text(self):
        pass

    def write_excel(self):
        pass
