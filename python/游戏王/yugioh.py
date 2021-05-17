import requests
from bs4 import BeautifulSoup
import re
import json

"""
爬虫卡查器，把所有卡片信息保存到数据库
"""

base_url = 'https://www.ourocg.cn/card'
list_url = base_url + '/list-5/{}'



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}

url = list_url.format(1)

resp = requests.get(url, headers=headers)
html = resp.content.decode('utf-8')
# print(html)

soup = BeautifulSoup(html,"lxml")
# 获取用正则<script>中window\.__STORE__变量的值
pattern = re.compile(r"window\.__STORE__ = (.*?);", re.MULTILINE | re.DOTALL)
script = soup.find("script", text=pattern)
# 爬取的json数据
data_json = pattern.search(script.text).group(1)

data_dic = json.loads(data_json)

for card in data_dic['cards']:
    print(card)

#TODO 把json数据保存到数据库
#TODO 下载图片，转成字符串保存到数据库

"""
{'id': '63503850', 'hash_id': 'YAco3MDP', 'password': '63503850', 'name': '蛮力攻击实施员', 'name_ja': None, 'name_en': None, 'locale': '1', 'type_st': '怪兽|效果|连接', 'type_val': '1', 'img_url': 'https://ocg-p.moekard.com/ygopro/pics/63503850.jpg', 'level': '2', 'attribute': '暗', 'race': '电子界', 'atk': '1600', 'def': '5', 'pend_l': None, 'pend_r': None, 'link': '2', 'link_arrow': '1,3', 
'name_nw': '蛮力攻击实施员', 'desc': '效果怪兽2只\r\n这个卡名的效果1回合只能使用1次。\r\n①：丢弃1张手卡，以对方场上1张表侧表示的卡为
对象才能发动。对方可以把原本种类（怪兽·魔法·陷阱）和那张表侧表示的卡相同的1张卡从手卡丢弃让这个效果无效。没丢弃的场合，作为对象的表 
侧表示的卡破坏。', 'desc_nw': '效果怪兽2只\r\n这个卡名的效果1回合只能使用1次。\r\n①：丢弃1张手卡，以对方场上1张表侧表示的卡为对象才 
能发动。对方可以把原本种类（怪兽·魔法·陷阱）和那张表侧表示的卡相同的1张卡从手卡丢弃让这个效果无效。没丢弃的场合，作为对象的表侧表示 
的卡破坏。', 'rare': None, 'package': None, 'href': 'https://www.ourocg.cn/card/YAco3MDP'}
"""