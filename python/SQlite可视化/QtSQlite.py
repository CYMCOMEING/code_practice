import sys
import sqlite3
from PyQt5.QtCore import pyqtSignal, QObject, QThread,QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel,QStandardItem

from Ui_QtSQlite import Ui_MainWindow


class QtSQlite(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QtSQlite, self).__init__(parent)
        self.setupUi(self)

        self.db = SQLiteTool()
        self.initUI()

    def initUI(self):
        # 不能对表格进行修改（双击重命名等）
        self.table_lw.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.open_db_action.triggered.connect(self.open_db)
        self.table_lw.doubleClicked.connect(self.show_data)

    def open_db(self):
        file = QFileDialog.getOpenFileName(
            self, "选择SQLite数据库", '.', "SQlite Files (*.db);;All Files (*)")

        self.db.close()
        self.db.open(file[0])
        tables = self.db.query("select name from sqlite_master where type='table' order by name;")
        self.table_lw.clear()
        self.table_lw.addItems(tables[0])

    def show_data(self, item):
        # info = self.db.query("select sql from sqlite_master where tbl_name = '{}' and type='table';".format(item.data()))
        info = self.db.query('PRAGMA table_info({});'.format(item.data()))
        """
        cid name type notnull dflt_value pk
        """
        # 字段数
        col = len(info)
        data = self.db.query('select * from {};'.format(item.data()))
        # print(data)
        # 数据数量
        row = len(data)
        # print(col, row)
        #设置数据层次结构，行列
        self.model=QStandardItemModel(row,col)
        #设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['标题1','标题2','标题3'])
        for row in range(4):
            for column in range(4):
                item=QStandardItem('row %s,column %s'%(row,column))
                #设置每个位置的文本值
                self.model.setItem(row,column,item)

        #实例化表格视图，设置模型为自定义的模型
        self.data_tw.setModel(self.model)
        #水平方向标签拓展剩下的窗口部分，填满表格
        self.data_tw.horizontalHeader().setStretchLastSection(True)
        #水平方向，表格大小拓展到适当的尺寸      
        self.data_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


class SQLiteTool():
    def __init__(self):
        self.db = None
        self.c = None

    def open(self, file):
        self.db = sqlite3.connect(file)
        self.c = self.db.cursor()

    def close(self):
        if self.c:
            self.c.close()
            self.c = None
        if self.db:
            self.db.close()
            self.db = None

    def execute(self, sql, param=None):
        """
        执行数据库的增、删、改
        sql：sql语句
        param：数据，可以是list或tuple，亦可是None
        retutn：成功返回True
        """
        try:
            if param is None:
                self.c.execute(sql)
            else:
                if type(param) is list:
                    self.c.executemany(sql, param)
                else:
                    self.c.execute(sql, param)
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print(e)
            return False, e
        if count > 0:
            return True
        else:
            return False

    def query(self, sql, param=None):
        """
        查询语句
        sql：sql语句
        param：参数,可为None
        retutn：成功返回True
        """
        if param is None:
            self.c.execute(sql)
        else:
            self.c.execute(sql, param)
        return self.c.fetchall()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    q = QtSQlite()
    q.show()
    sys.exit(app.exec_())
