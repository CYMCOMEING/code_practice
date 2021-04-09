import json
import os
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from MyTools import dei_blankline, get_dir_files

chrome_driver_path = "D:\\git\\chromedriver.exe"
pic = os.path.abspath(".\\pic.jpg")

def search_pic():
    # 初始化浏览器
    try:
        chrome_options = Options()
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    except Exception as e:
        print("init_drive:", e)
        exit(1)

    # 等待超时
    driver.implicitly_wait(10)
    # 页面加载时间
    driver.set_page_load_timeout(30)
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
        with open('sauce.html', 'w', encoding="utf-8") as f:
            f.write(html)
        # parse_result(html)
        # 获取搜索结果
        # divs = driver.find_elements_by_xpath('//div[@class="result"]')
        # result_list = []
        # for div in divs:
        #     # print(div.find_element_by_xpath('//div[@class="resultimage"]/a').get_attribute('href'))
        #     result_list.append(dei_blankline(div.text))
            

        # result_dic = {'source': pic, 'results': result_list}
        # print(result_dic)
        # result_json = json.dumps(result_dic, ensure_ascii=False)
    except Exception as e:
        print(e)
    finally:
        if driver:
            driver.close()
        return result_json

def parse_result(html):
    soup = BeautifulSoup(html, features="lxml")
    result_all = soup.find_all('div',{'class':'result'})
    for res in result_all:
        tds = res.find_all('td')
        # print(tds[0].img['src'])
        # print(tds[1].prettify())
        # similarity = tds[1].find('div',class_="resultsimilarityinfo").text
        # title = tds[1].find('div',class_="resulttitle").text
        contentcolumn = tds[1].find('div',class_="resultcontentcolumn")
        cc = ''
        for child in contentcolumn.children:
            print(child)
            if child.name == 'br':
                cc += '\n'
            elif child.name:
                cc += child.text
        print(cc)
        print('\n')


if __name__ == "__main__":
    # print(search_pic())
    with open('sauce.html', 'r', encoding="utf-8") as f:
        html = f.read()

    parse_result(html)