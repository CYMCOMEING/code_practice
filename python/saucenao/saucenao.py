import json
import os
import sys
import threading

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QFileDialog, QWidget
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from MyTools import dei_blankline, get_dir_files
from saucenao_ui import Ui_Form

# chrome_driver_path = "G:\\Project\\python\\picmanage\\chromedriver.exe"
chrome_driver_path = "D:\\git\\chromedriver.exe"


class SauceNAO:
    save_path = r'E:\1111\fullcomber\pic\待搜索图片'

    def __init__(self):
        self.driver = None
        self.th = None
        self.isExit = False

    def __del__(self):
        if self.driver:
            self.driver.close()

    def init_drive(self):
        """
        初始化浏览器
        :return:
        """
        try:
            chrome_options = Options()
            # chrome_options.add_argument('headless')
            self.driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
            # 等待超时
            self.driver.implicitly_wait(10)
            # 页面加载时间
            self.driver.set_page_load_timeout(30)
            self.driver.get('https://saucenao.com/')
        except Exception as e:
            print("init_drive:", e)
            self.driver.close()
            exit(1)

    def search_pic(self, pic):
        """
        搜索单个图片
        :param pic: 要搜索图片
        :return: 返回结果，json格式
        """
        try:
            # 上传图片
            input = self.driver.find_element_by_xpath('//input[@id="file"]')
            input.send_keys(pic)
            # 点击搜索
            self.driver.find_element_by_xpath('//input[@value="get sauce"]').click()
            # html = self.driver.page_source
            # print(html)
            # 获取搜索结果
            divs = self.driver.find_elements_by_xpath('//div[@class="result"]')
            result_list = []
            for div in divs:
                # print(div.find_element_by_xpath('//div[@class="resultimage"]/a').get_attribute('href'))
                result_list.append(dei_blankline(div.text))

            result_dic = {'source': pic, 'results': result_list}
            # print(result_dic)
            result_json = json.dumps(result_dic, ensure_ascii=False)
            return result_json
        except Exception as e:
            print(e)
            return ''

    def search_list(self, pic_list):
        """
        搜索列表里面的图片
        :param pic_list:
        :return:
        """
        with open('saucenao_result.txt', 'a', encoding='utf-8') as f:
            i = 1
            for pic in pic_list:
                res_json = self.search_pic(pic)
                if res_json:
                    f.write(res_json + '\n')
                    print(str(i) + " 完成 " + pic)
                else:
                    print(str(i) + " 失败 " + pic)
                i = i + 1
                if self.isExit:
                    break

    def start(self, save_path=save_path):
        """
        开始搜索
        先找过滤已经搜索的图片再搜索
        :param save_path:
        :return:
        """

        # 过滤已经搜多的图片
        dir_list = get_dir_files(save_path)
        if os.path.exists('saucenao_result.txt'):
            with open('saucenao_result.txt', mode='r', encoding='utf-8') as f:
                for result_json in f.readlines():
                    source_pic = json.loads(result_json)['source']
                    dir_list.remove(source_pic)
                    # print(result_json)

        if dir_list:
            self.search_list(dir_list)

    def start_in_thread(self, save_path=save_path):
        self.th = threading.Thread(target=self.start, args=(save_path,))
        self.th.start()
        self.isExit = False

    def wait_thead(self):
        if self.th:
            self.isExit = True
            self.th.join()

class SauceNAOUi(QWidget, Ui_Form):
    """
    1. 显示文件列表
    2. 点击列表项显示结果
    3. 输入pid，打开指定网页
    """

    def __init__(self, parent=None):
        super(SauceNAOUi, self).__init__(parent)
        self.setupUi(self)

        # 逻辑对象实例
        self.sn = SauceNAO()
        self.sn.init_drive()

        # 获取保存路径
        self.path_line_edit.setText(self.sn.save_path)

        self.pic_list_widget.doubleClicked.connect(self._show_result_detail)

        # 下拉列表
        self.type_combo_box.addItem('PID')
        self.type_combo_box.addItem('USERID')

        # 打开按钮点击事件
        self.open_push_button.clicked.connect(self._clicked_open_push)

        # 搜索按钮按点击事件
        self.search_button.clicked.connect(self._clicked_search)

        # 停止搜索按钮点击事件
        self.stop_button.clicked.connect(self._clicked_stop)

        # 刷新按钮点击事件
        self.refresh_button.clicked.connect(self._refresh_stop)

        # 选择文件按钮点击事件
        self.choice_button.clicked.connect(self._clicked_choice)

        # 打开文件按钮点击事件
        self.open_dir_button.clicked.connect(self._clicked_open_dir)

        # 主数据列表
        self._refresh_stop()

    def _clicked_open_dir(self):
        os.startfile(self.path_line_edit.text())

    def _clicked_choice(self):
        path = QFileDialog.getExistingDirectory(self, '请选择文件夹路径', '.', options=QFileDialog.ShowDirsOnly)
        if path and os.path.exists(path):
            self.sn.save_path = path
            self.path_line_edit.setText(path)

    def _clicked_search(self):
        self.sn.start_in_thread()

    def _clicked_stop(self):
        self.sn.wait_thead()

    def _refresh_stop(self):
        self.resulit_list = self.load_data()
        # 显示文件列表
        self._show_resulit_list()

    def _clicked_open_push(self):
        """
        打开连接
        :return:
        """
        text = self.id_line_edit.text()
        if text:
            type_id = self.type_combo_box.currentText()
            if type_id == 'PID':
                url = 'https://www.pixiv.net/artworks/{}'.format(text)
            elif type_id == 'USERID':
                url = 'https://www.pixiv.net/users/{}'.format(text)
            print(url)
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))
            # import webbrowser
            # webbrowser.open(url, new=0, autoraise=True)
            # webbrowser.open_new(url)
            # webbrowser.open_new_tab(url)

    def _show_resulit_list(self):
        """
        显示索引列表
        :return:
        """
        if not self.resulit_list:
            return

        for item in self.resulit_list:

            self.pic_list_widget.addItem(QListWidgetItem(os.path.basename(item['source'])))

    def _show_result_detail(self, qModelIndex):
        if not self.resulit_list:
            return
        pic_path = qModelIndex.data()
        for results in self.resulit_list:
            if results['source'] == pic_path:
                self.resulit_text_browser.clear()
                for result in results['results']:
                    self.resulit_text_browser.append(result + '\n' * 2)
                break

    def load_data(self):
        data = []
        with open('saucenao_result.txt', mode='r', encoding='utf-8') as f:
            data = f.readlines()
        return [json.loads(i) for i in data]


if __name__ == '__main__':
    # sn = SauceNAO()
    # sn.start(r'E:\1111\fullcomber\pic\待搜索图片')
    app = QApplication(sys.argv)
    w = SauceNAOUi()
    w.show()
    sys.exit(app.exec_())
