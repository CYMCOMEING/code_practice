import sys
import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap

from Ui_demo import Ui_Form


class LoadPic(QObject):
    file_list = []
    show_pic_signal = pyqtSignal(QPixmap)
    isQuit = False

    def __init__(self):
        super(LoadPic, self).__init__()

    def load(self):
        self.isQuit = False
        for file in self.file_list:
            if self.isQuit:
                break
            pix = QPixmap(file)
            self.show_pic_signal.emit(pix)
            time.sleep(1)

    def stop(self):
        self.isQuit = True


class Demo(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.readpic)
        self.pushButton_2.clicked.connect(self.tStop)
        self.lbs = [self.label, self.label_2, self.label_3,
                    self.label_4, self.label_5, self.label_6]
        self.index = 0

        self.loadpic = LoadPic()
        self.loadpic.file_list = ["pic_1.jpg", "pic_2.jpg",
                                  "pic_3.jpg", "pic_4.jpg", "pic_5.jpg", "pic_6.jpg"]
        self.t = QThread()

        self.loadpic.show_pic_signal.connect(self.flush)
        self.loadpic.moveToThread(self.t)
        self.t.started.connect(self.loadpic.load)
        self.t.finished.connect(self.finished)

    def readpic(self):
        self.t.start()

    def flush(self, pix):
        lb = self.lbs[self.index]
        self.index = self.index + 1 if self.index < 6 else 0
        lb.setScaledContents(True)
        lb.setPixmap(pix)

    def finished(self):
        print("完成")

    def tStop(self):
        # 手动停止
        self.index = 0
        self.loadpic.stop()
        self.t.quit()
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    d = Demo()
    d.show()
    sys.exit(app.exec_())
