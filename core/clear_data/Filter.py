import re

from bs4 import BeautifulSoup


class FilterData:
    def __init__(self, total_text):
        self.total_text = total_text

    # 针对纯html页面，这段是ai找的，实测还是能应对多数情况
    def remove_html_tags(self):
        text = re.sub(r'<!--.*?-->', '', self.total_text, flags=re.DOTALL)
        soup = BeautifulSoup(text, "html.parser")
        text = ' '.join(soup.stripped_strings)
        text = re.sub(r'&[a-z]+;', ' ', text)
        cleaned_text = re.sub(r'\s+', ' ', text).strip()
        return cleaned_text

    def split_text(self):
        pass

    def response_text(self):
        pass
