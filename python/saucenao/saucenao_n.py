import json
import os
import sys
from bs4 import BeautifulSoup,element
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from MyTools import dei_blankline, get_dir_files

chrome_driver_path = "D:\\git\\chromedriver.exe"
pic = os.path.abspath(".\\pic.jpg")

# 搜索图片，爬取结果
def search_pic():
    # 初始化浏览器
    try:
        chrome_options = Options()
        # chrome_options.add_argument('headless')
        driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    except Exception as e:
        print("init_drive:", e)
        exit(1)

    # 等待超时
    driver.implicitly_wait(10)
    # 页面加载时间
    # driver.set_page_load_timeout(30)
    driver.get('https://saucenao.com/')

    # 搜索单个图片
    try:
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
        print(result_dic)
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
    result_all = soup.find_all('div',class_='result')
    res_list = []
    for res in result_all:
        tds = res.find_all('td')
        # 图片链接
        img_url = tds[0].img['src']
        # 相似度
        columnstr = tds[1].find('div',class_="resultsimilarityinfo").text + '\n'
        # 标题
        columnstr += tds[1].find('div',class_="resulttitle").text + '\n'
        # 每列内容,提取所有字符串，<br>替换成换行符
        contentcolumn = tds[1].find('div',class_="resultcontentcolumn")
        for child in contentcolumn.children:
            if child.name and child.name == 'br':
                columnstr += '\n'
            elif child.string:
                columnstr += child.string
        res_list.append({'img': img_url, 'content':columnstr})
    return res_list

# 下载搜索的对比图
def download_img(res_list):
    # TODO 根据源文件生成文件名，统一存放在一个目录
    # TODO 下载好文件后，原本url替换成本地相对路径
    # TODO 改进，由于文件不大，可以将文件转成字符串保存在数据库
    for i in range(len(res_list['results'])):
        # print(res_list['results'][i]['img'])
        r = requests.get(res_list['results'][i]['img'])
        with open('aaa_{}.jpg'.format(i), 'wb') as f:
            f.write(r.content)  

'''
数据库表头格式
source      results
源文件名    搜索结果(json字符串)

搜索结果json格式
[{'img':},{'content':}]
img原本是url，下载好后替换成文件路径
'''

if __name__ == "__main__":
    # print(search_pic())
    with open('test.html','r',encoding='utf-8') as f:
        html = f.read()
    res_data = parse_result(html)
    result_dic = {'source': "aaa.jpg", 'results': res_data}

    download_img(result_dic)
    # result_json = json.dumps(result_dic, ensure_ascii=False)
    # print(result_json)
    