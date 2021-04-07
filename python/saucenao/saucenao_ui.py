# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saucenao_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(624, 393)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.resulit_text_browser = QtWidgets.QTextBrowser(Form)
        self.resulit_text_browser.setObjectName("resulit_text_browser")
        self.gridLayout.addWidget(self.resulit_text_browser, 1, 3, 1, 4)
        self.search_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy)
        self.search_button.setObjectName("search_button")
        self.gridLayout.addWidget(self.search_button, 2, 0, 1, 1)
        self.type_combo_box = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_combo_box.sizePolicy().hasHeightForWidth())
        self.type_combo_box.setSizePolicy(sizePolicy)
        self.type_combo_box.setObjectName("type_combo_box")
        self.gridLayout.addWidget(self.type_combo_box, 2, 3, 1, 1)
        self.id_line_edit = QtWidgets.QLineEdit(Form)
        self.id_line_edit.setObjectName("id_line_edit")
        self.gridLayout.addWidget(self.id_line_edit, 2, 4, 1, 1)
        self.path_line_edit = QtWidgets.QLineEdit(Form)
        self.path_line_edit.setObjectName("path_line_edit")
        self.gridLayout.addWidget(self.path_line_edit, 0, 0, 1, 5)
        self.open_push_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_push_button.sizePolicy().hasHeightForWidth())
        self.open_push_button.setSizePolicy(sizePolicy)
        self.open_push_button.setObjectName("open_push_button")
        self.gridLayout.addWidget(self.open_push_button, 2, 6, 1, 1)
        self.pic_list_widget = QtWidgets.QListWidget(Form)
        self.pic_list_widget.setObjectName("pic_list_widget")
        self.gridLayout.addWidget(self.pic_list_widget, 1, 0, 1, 3)
        self.choice_button = QtWidgets.QPushButton(Form)
        self.choice_button.setObjectName("choice_button")
        self.gridLayout.addWidget(self.choice_button, 0, 5, 1, 1)
        self.open_dir_button = QtWidgets.QPushButton(Form)
        self.open_dir_button.setObjectName("open_dir_button")
        self.gridLayout.addWidget(self.open_dir_button, 0, 6, 1, 1)
        self.stop_button = QtWidgets.QPushButton(Form)
        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button, 2, 1, 1, 1)
        self.refresh_button = QtWidgets.QPushButton(Form)
        self.refresh_button.setObjectName("refresh_button")
        self.gridLayout.addWidget(self.refresh_button, 2, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search_button.setText(_translate("Form", "搜索"))
        self.open_push_button.setText(_translate("Form", "打开"))
        self.choice_button.setText(_translate("Form", "选择文件夹"))
        self.open_dir_button.setText(_translate("Form", "打开文件夹"))
        self.stop_button.setText(_translate("Form", "停止"))
        self.refresh_button.setText(_translate("Form", "刷新"))
