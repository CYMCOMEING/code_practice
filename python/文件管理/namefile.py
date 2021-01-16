"""
win10已经没有复移动文件时，遇到的同名可以自动重命名的功能
"""

import sys
import os
from shutil import copy2, move
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAbstractItemView

from Ui_nameflie import Ui_MainWindow


class NameFile(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(NameFile, self).__init__(parent)
        self.setupUi(self)

        self.init()

    def init(self):
        self.open_l_btn.clicked.connect(lambda: self.open_dir(True))
        self.open_r_btn.clicked.connect(lambda: self.open_dir(False))
        self.copy_l_btn.clicked.connect(
            lambda: self.operate_file(True, 'copy'))
        self.copy_r_btn.clicked.connect(
            lambda: self.operate_file(False, 'copy'))
        self.move_l_btn.clicked.connect(
            lambda: self.operate_file(True, 'move'))
        self.move_r_btn.clicked.connect(
            lambda: self.operate_file(False, 'move'))
        # 不能对表格进行修改（双击重命名等）
        self.l_lw.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.l_lw.setSelectionMode(
            QAbstractItemView.ExtendedSelection)  # 按住CTRL可多选
        self.r_lw.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.r_lw.setSelectionMode(
            QAbstractItemView.ExtendedSelection)  # 按住CTRL可多选

    def open_dir(self, isLeft):
        dir = QFileDialog.getExistingDirectory()
        if dir:
            self.setlist(isLeft, dir)

    def setlist(self, isLeft, dir):
        if isLeft:
            le = self.l_le
            lw = self.l_lw
        else:
            le = self.r_le
            lw = self.r_lw

        le.setText(dir)
        file_list = []
        for file in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, file)):
                file_list.append(file)

        lw.clear()
        lw.addItems(file_list)

    def operate_file(self, isLeft, mode):
        if isLeft:
            le = self.l_le
            to_le = self.r_le
            lw = self.l_lw
        else:
            le = self.r_le
            to_le = self.l_le
            lw = self.r_lw

        select_files = lw.selectedItems()
        if select_files and to_le.text():
            for i in select_files:
                # 生成目标路径
                new_paht = name_file(os.path.join(
                    le.text(), i.text()), to_le.text())
                if new_paht:
                    if mode == 'move':
                        move(os.path.join(le.text(), i.text()), new_paht)
                    else:
                        copy2(os.path.join(le.text(), i.text()), new_paht)

            self.setlist(bool(1-isLeft), to_le.text())
            self.setlist(isLeft, le.text())


def name_file(file_path, target_path):
    file = os.path.abspath(file_path)
    new_name = ''

    if os.path.exists(file) and os.path.exists(target_path) and os.path.isdir(target_path):
        name = os.path.splitext(os.path.split(file)[1])
        new_name = os.path.join(target_path, name[0]+name[1])

        if os.path.exists(new_name):
            index = 1
            while True:
                new_name = new_name = os.path.join(
                    target_path, '{} ({}){}'.format(name[0], index, name[1]))
                if not os.path.exists(new_name):
                    break
                index += 1

    return os.path.abspath(new_name)


def copy_file(file, target_path):
    pass


def move_file(file, target_path):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    nf = NameFile()
    nf.show()
    sys.exit(app.exec_())
