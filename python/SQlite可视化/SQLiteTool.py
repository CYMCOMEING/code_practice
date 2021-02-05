class SQLiteTool():
    def __init__(self):
        self.db = None
        self.c = None
        self.isOpen = False

    def open(self, file):
        self.db = sqlite3.connect(file)
        self.c = self.db.cursor()
        self.isOpen = True

    def close(self):
        if self.c:
            self.c.close()
            self.c = None
        if self.db:
            self.db.close()
            self.db = None
            self.isOpen = False

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
