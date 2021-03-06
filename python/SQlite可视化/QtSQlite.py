import sys
import sqlite3
from PyQt5.QtCore import pyqtSignal, QObject, QThread, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAbstractItemView, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Ui_QtSQlite import Ui_MainWindow
from SQLiteTool import SQLiteTool


class QtSQlite(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QtSQlite, self).__init__(parent)
        self.setupUi(self)

        self.db = SQLiteTool()
        self.initUI()

    def initUI(self):
        """
        ui控件初始化，绑定事件
        """
        # 不能对表格进行修改（双击重命名等）
        self.table_lw.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 水平方向标签拓展剩下的窗口部分，填满表格
        self.data_tw.horizontalHeader().setStretchLastSection(True)
        # 水平方向，表格自适应大小
        self.data_tw.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 打开菜单
        self.open_db_action.triggered.connect(self.open_db)
        # 表名列表双击
        self.table_lw.doubleClicked.connect(self.show_data)
        # 回车事件
        self.sql_le.returnPressed.connect(self.run_sql)

    def open_db(self):
        """
        打开数据库，在ui显示所有表名
        """
        file = QFileDialog.getOpenFileName(
            self, "选择SQLite数据库", '.', "SQlite Files (*.db);;All Files (*)")

        if file:
            self.db.close()
            self.db.open(file[0])
            tables = self.db.query(
                "select name from sqlite_master where type='table' order by name;")
            self.table_lw.clear()
            self.table_lw.addItems(tables[0])

    def show_data(self, item):
        """
        ui显示数据库数据
        """
        # infos = self.db.query("select sql from sqlite_master where tbl_name = '{}' and type='table';".format(item.data()))

        # 字段类型 cid name type notnull dflt_value pk
        infos = self.db.query('PRAGMA table_info({});'.format(item.data()))
        # 字段数
        col = len(infos)

        # 表头
        key_head = []
        for info in infos:
            key_head.append(info[1])

        # 获取表所有数据
        table_data = self.db.query('select * from {};'.format(item.data()))
        # 数据数量
        row = len(table_data)

        # 设置数据层次结构，行列
        self.model = QStandardItemModel(row, col)

        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(key_head)
        for r in range(row):
            for c in range(col):
                item = QStandardItem(str(table_data[r][c]))
                # 设置每个位置的文本值
                self.model.setItem(r, c, item)

        # 实例化表格视图，设置模型为自定义的模型
        self.data_tw.setModel(self.model)

    def run_sql(self):
        sql = self.sql_le.text()
        result_data = ""
        if sql == 'help':
            result_data = sql_help
        elif self.db.isOpen:
            result_data = self.db.query(sql)
            # self.result_te.setText(result_data)
            print(result_data)
        else:
            return
        self.sql_le.setText("")
        self.result_te.setText(result_data)

sql_help = """create table tablename (id int not null,name text not null,age int);

insert into tablename (id,name,age) values (?,?,?);

select * from tablename;
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    q = QtSQlite()
    q.show()
    sys.exit(app.exec_())
