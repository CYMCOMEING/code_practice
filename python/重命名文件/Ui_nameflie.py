# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\git\python\nameflie.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 362)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_l_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_l_btn.setObjectName("open_l_btn")
        self.horizontalLayout.addWidget(self.open_l_btn)
        self.l_le = QtWidgets.QLineEdit(self.centralwidget)
        self.l_le.setObjectName("l_le")
        self.horizontalLayout.addWidget(self.l_le)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.open_r_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_r_btn.setObjectName("open_r_btn")
        self.horizontalLayout_2.addWidget(self.open_r_btn)
        self.r_le = QtWidgets.QLineEdit(self.centralwidget)
        self.r_le.setObjectName("r_le")
        self.horizontalLayout_2.addWidget(self.r_le)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.copy_l_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copy_l_btn.setObjectName("copy_l_btn")
        self.verticalLayout.addWidget(self.copy_l_btn)
        self.move_l_btn = QtWidgets.QPushButton(self.centralwidget)
        self.move_l_btn.setObjectName("move_l_btn")
        self.verticalLayout.addWidget(self.move_l_btn)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.copy_r_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copy_r_btn.setObjectName("copy_r_btn")
        self.verticalLayout_2.addWidget(self.copy_r_btn)
        self.move_r_btn = QtWidgets.QPushButton(self.centralwidget)
        self.move_r_btn.setObjectName("move_r_btn")
        self.verticalLayout_2.addWidget(self.move_r_btn)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.l_lw = QtWidgets.QListWidget(self.centralwidget)
        self.l_lw.setObjectName("l_lw")
        self.gridLayout.addWidget(self.l_lw, 1, 0, 1, 1)
        self.r_lw = QtWidgets.QListWidget(self.centralwidget)
        self.r_lw.setObjectName("r_lw")
        self.gridLayout.addWidget(self.r_lw, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 23))
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
        self.open_l_btn.setText(_translate("MainWindow", "打开目录"))
        self.open_r_btn.setText(_translate("MainWindow", "打开目录"))
        self.copy_l_btn.setText(_translate("MainWindow", "复制>>"))
        self.move_l_btn.setText(_translate("MainWindow", "移动>>"))
        self.copy_r_btn.setText(_translate("MainWindow", "<<复制"))
        self.move_r_btn.setText(_translate("MainWindow", "<<移动"))
