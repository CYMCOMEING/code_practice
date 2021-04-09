import json
import os
import sys
from bs4 import BeautifulSoup,element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from MyTools import dei_blankline, get_dir_files

chrome_driver_path = "D:\\git\\chromedriver.exe"
pic = os.path.abspath(".\\pic.jpg")

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
        result_json = ''
        # 上传图片
        input = driver.find_element_by_xpath('//input[@id="fileInput"]')
        input.send_keys(pic)
        # 点击搜索
        driver.find_element_by_xpath('//input[@id="searchButton"]').click()
        html = driver.page_source
        # print(html)
        # 获取搜索结果
        res_data = parse_result(html)
        
        result_dic = {'source': pic, 'results': res_data}
        print(result_dic)
        result_json = json.dumps(result_dic, ensure_ascii=False)
    except Exception as e:
        print(e)
    finally:
        if driver:
            driver.close()
        return result_json

def parse_result(html):
    soup = BeautifulSoup(html, features="lxml")
    result_all = soup.find_all('div',{'class':'result'})
    res_list = []
    for res in result_all:
        tds = res.find_all('td')
        # 图片链接
        img_src = tds[0].img['src']
        # 相似度
        similarity = tds[1].find('div',class_="resultsimilarityinfo").text
        # 标题
        columnstr = tds[1].find('div',class_="resulttitle").text
        # 每列内容
        contentcolumn = tds[1].find('div',class_="resultcontentcolumn")
        columnstr += '\n'
        for child in contentcolumn.children:
            if child.name and child.name == 'br':
                columnstr += '\n'
            elif child.string:
                columnstr += child.string
        res_list.append({'img': img_src, 'similarity':similarity, 'content':columnstr})
    return res_list


if __name__ == "__main__":
    print(search_pic())