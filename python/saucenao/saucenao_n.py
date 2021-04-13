import json
import os
import sys
from bs4 import BeautifulSoup, element
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
from io import BytesIO
from PIL import Image

from MyTools import dei_blankline, get_dir_files
from sdb import SDB

chrome_driver_path = os.path.abspath("D:\\git\\chromedriver.exe")
# System.setProperty("webdriver.chrome.driver", chrome_driver_path)
PIC = os.path.abspath(".\\pic.jpg")


def init_chrome():
    # 初始化浏览器
    try:
        chrome_options = Options()
        # 无头模式
        chrome_options.add_argument('headless')

        driver = webdriver.Chrome(
            executable_path=chrome_driver_path, chrome_options=chrome_options)
    except Exception as e:
        print("init_drive:", e)
        exit(1)

    # 等待超时
    driver.implicitly_wait(10)
    # 页面加载时间
    # driver.set_page_load_timeout(30)
    return driver

# 搜索图片，爬取结果
def search_pic(driver, pic):
    # 搜索单个图片
    try:
        driver.get('https://saucenao.com/')
        # result_json = ''
        result_dic = {'source': pic, 'results': []}
        # 上传图片
        input = driver.find_element_by_xpath('//input[@id="fileInput"]')
        input.send_keys(pic)
        # 点击搜索
        driver.find_element_by_xpath('//input[@id="searchButton"]').click()
        html = driver.page_source
        # with open('test.html', 'w',encoding='utf-8') as f:
        #     f.write(html)
        # print(html)
        # 获取搜索结果
        res_data = parse_result(html)

        result_dic['results'] = res_data
        # print(result_dic)
        # result_json = json.dumps(result_dic, ensure_ascii=False)
    except Exception as e:
        print(e)
    finally:
        if driver:
            driver.close()
        # return result_json
        return result_dic

# 提取网页搜索结果数据
def parse_result(html):
    soup = BeautifulSoup(html, features="lxml")
    result_all = soup.find_all('div', class_='result')
    res_list = []
    for res in result_all:
        tds = res.find_all('td')
        # 图片链接
        img_url = tds[0].img['src']
        # 相似度
        columnstr = tds[1].find(
            'div', class_="resultsimilarityinfo").text + '\n'
        # 标题
        columnstr += tds[1].find('div', class_="resulttitle").text + '\n'
        # 每列内容,提取所有字符串，<br>替换成换行符
        contentcolumn = tds[1].find('div', class_="resultcontentcolumn")
        for child in contentcolumn.children:
            if child.name and child.name == 'br':
                columnstr += '\n'
            elif child.string:
                columnstr += child.string
        res_list.append({'img': img_url, 'data': '', 'content': columnstr})
    return res_list

# 下载搜索的对比图
def download_img(res_dic):
    for i in range(len(res_dic['results'])):
        r = requests.get(res_dic['results'][i]['img'])
        res_dic['results'][i]['data'] = pic2str(r.content)

# 图片转字符串
def pic2str(buf):
    buffer = BytesIO()
    buffer.write(buf)
    b = buffer.getvalue()
    return base64.b64encode(b).decode("utf-8")

# 字符串转图片
def str2pic(str):
    b = base64.b64decode(str.encode("utf-8"))
    buffer = BytesIO(b)
    return buffer

def dict2json(dict):
    return json.dumps(dict, ensure_ascii=False)

def json2dict(j):
    return json.loads(j)

def run():
    # 读取目录图片
    pic_list = [PIC]
    # 打开数据库
    db = SDB()
    # 初始化浏览器
    chrome = init_chrome()
    # 搜索图片
    result_dic = search_pic(chrome, pic_list[0])
    # 下载搜图结果图片,并转成字符串保存
    download_img(result_dic)
    # 将部分数据转字符串
    result_dic['results'] = dict2json(result_dic['results'])
    # 写入数据库
    db.add(result_dic)
    # 查看数据
    print(db.read_all())

def read():
    # 打开数据库
    db = SDB()
    data_str = db.read_all()
    # print(data_str[0][1])
    dict = json2dict(data_str[0][1])
    print(dict[0]['img'])
    f = str2pic(dict[0]['data'])
    img = Image.open(f)
    img.show()

if __name__ == "__main__":
    # print(search_pic())
    # with open('test.html', 'r', encoding='utf-8') as f:
    #     html = f.read()
    # res_data = parse_result(html)
    # result_dic = {'source': "aaa.jpg", 'results': res_data}

    # download_img(result_dic)
    # result_json = json.dumps(result_dic, ensure_ascii=False)
    # print(result_json)

    # run()
    read()
