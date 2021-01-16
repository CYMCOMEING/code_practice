import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QAbstractItemView

from Ui_rar_file import Ui_rarfile_form
from RarTool import un_file


class RarFile(QWidget, Ui_rarfile_form):
    def __init__(self, parent=None):
        super(RarFile, self).__init__(parent)
        self.setupUi(self)

        self.initUi()

    def initUi(self):
        # 不能对表格进行修改（双击重命名等）
        self.file_lw.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 按住CTRL可多选
        self.file_lw.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.open_dir_btn.clicked.connect(self.open_dir)
        self.cur_rbtn.clicked.connect(lambda: self.unrar_choice(self.cur_rbtn))
        self.self_rbtn.clicked.connect(
            lambda: self.unrar_choice(self.self_rbtn))
        self.other_rbtn.clicked.connect(
            lambda: self.unrar_choice(self.other_rbtn))
        self.unrar_btn.clicked.connect(self.unrar_file)

    def open_dir(self):
        # 读取目录在ui上显示
        dir = QFileDialog.getExistingDirectory()
        if dir:
            self.setlist(dir)
            self.path_le.setText(dir)
            self.unrar_path = dir

    def setlist(self, dir):
        # 读取目录下的文件在ui显示
        file_list = []
        for file in os.listdir(dir):
            # TODO 过滤出rar zip文件
            if os.path.isfile(os.path.join(dir, file)):
                file_list.append(file)

        self.file_lw.clear()
        self.file_lw.addItems(file_list)

    def unrar_choice(self, btn):
        # 单选按钮被选择事件处理
        if btn == self.other_rbtn:
            dir = QFileDialog.getExistingDirectory()
            if dir:
                self.other_path_le.setText(dir)
            else:
                self.other_path_le.setText('')
            self.other_path_le.setEnabled(True)
        else:
            self.other_path_le.setEnabled(False)

    def unrar_file(self):
        select_files = self.file_lw.selectedItems()
        open_dir = self.path_le.text()
        if select_files and open_dir:
            for i in select_files:
                source_file = os.path.join(open_dir, i.text())
                target_dir = self.get_unrar_path(i.text())
                pwd = self.pwd_le.text()

                print(source_file, target_dir, pwd)
                # TODO 在线程下实现
                # un_file(source_file, target_dir, pwd)

    def get_unrar_path(self, rarfile):
        # 获取解压路径
        if self.cur_rbtn.isChecked():
            return self.path_le.text()

        if self.self_rbtn.isChecked():
            return os.path.join(self.path_le.text(), os.path.splitext(rarfile)[0])

        if self.other_rbtn.isChecked():
            return self.other_path_le.text()

        return ''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rf = RarFile()
    rf.show()
    sys.exit(app.exec_())
