# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\git\code_practice\python\saucenao\saucenao_n_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pic_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.pic_listWidget.setObjectName("pic_listWidget")
        self.horizontalLayout_2.addWidget(self.pic_listWidget)
        self.result_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.result_listWidget.setObjectName("result_listWidget")
        self.horizontalLayout_2.addWidget(self.result_listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pic_label = QtWidgets.QLabel(self.centralwidget)
        self.pic_label.setText("")
        self.pic_label.setObjectName("pic_label")
        self.horizontalLayout.addWidget(self.pic_label)
        self.pic_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.pic_textEdit.setObjectName("pic_textEdit")
        self.horizontalLayout.addWidget(self.pic_textEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))