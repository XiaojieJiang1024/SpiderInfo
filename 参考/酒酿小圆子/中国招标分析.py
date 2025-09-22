from bs4 import BeautifulSoup


with open('response.html', 'r', encoding='utf-8') as f:
    response_text = f.read()

page = BeautifulSoup(response_text, 'html.parser')
ul = page.find('ul', attrs={'class': 'vT-srch-result-list-bid'})
# print(ul)
# print("=====")
li_list = ul.find_all('li')

def make_china_string(li):
    # data_str = ""
    # href = li.find('a')
    title = li.find('a').get_text(strip=True)
    items = li.find('span').get_text(separator='|', strip=True).split('|')
    timestamp = items[0]
    buyer = items[1].replace('采购人：', '')
    agency = items[2].replace('代理机构：', '')
    data_str = title + ' ' + buyer.strip() + ' ' + agency + ' ' + timestamp + '\n'
    return data_str


# print(make_string(li_list[0]))
total_china_str = ''
for li in li_list:
    total_china_str += make_china_string(li)

print(total_china_str)

# 河南省档案馆中福公司英文档案整理与开发项目流标公告 国家档案局  中钰招标有限公司 2025.06.09 10:22:12

# 三门峡市交通运输局河南省三门峡市公共交通公司更新68台老旧公交车项目-公开招标公告 三门峡市交通运输局  三门峡市政府采购服务中心 2025.06.05 17:14:08