import sqlite3
import os

"""
PicData
id, path,remake,cosin,similar, ahash, dhash

CompareData
id1, id2, cosin, similar, ahash, dhash
"""


class picSql():
    def __init__(self):
        self.filename = "picSql.db"
        self.db = None
        self.c = None

    def open(self):
        self.db = sqlite3.connect(self.filename)
        self.c = self.db.cursor()
        return self

    def close(self):
        """
        关闭数据库
        """
        self.c.close()
        self.db.close()
        self.db = None
        self.c = None

    def create_table(self, sql):
        try:
            self.c.execute(sql)
        except Exception as e:
            print("create table fail. " + str(e))

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
            print(e, sql)
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
        try:
            if param is None:
                self.c.execute(sql)
            else:
                self.c.execute(sql, param)
        except Exception as e:
            print(e, sql)

        return self.c.fetchall()

    def get_cursor_head(self):
        return [tuple[0] for tuple in self.c.description]

    # 支持with
    def __enter__(self):
        return self.open()

    def __exit__(self, type, value, trace):
        print(type, value, trace)
        self.close()


if __name__ == "__main__":
    # ps = picSql().open()
    # ps.add_pic("D:\\dddd.jpg")
    # ps.add_pic("D:\\hhhh.jpg")
    # ps.add_pic("D:\\yyyy.jpg")
    # print(ps.search_all("*"), "\n")
    # ps.modify_pic(["id",1], ("cosin",), ("SDFAFHSJLDF",))

    # ps.modify_pic(["id",3], ("cosin", "similar", "hash"), ("SDFALNAGDS", "SFDREGTJYTJ", "LSDHGDKLGJU"))
    # ps.modify_pic(["path","D:\\hhhh.jpg"], ("cosin", "similar", "hash"), ("SDFALNAGDS", "SFDREGTJYTJ", "LSDHGDKLGJU"))

    # print(ps.search_all("*"), "\n")

    # ps.del_pic(["id", 2])
    # print(ps.search_all("*"), "\n")

    # print(ps.search_all("path, hash"), "\n")

    # print(ps.search_one(["id", 3], "path, similar, hash"), "\n")
    ############
    # ps.add_comp(id1=3, id2=4, cosin="sadff", similar="sdffsd", hash="sdfasf")
    # ps.add_comp(id1=6, id2=4, cosin="sadff", similar="sdffsd", hash="sdfasf")
    # ps.add_comp(id1=6, id2=8, cosin="sadff", similar="sdffsd", hash="sdfasf")

    # print(*ps.search_comp_id(4, "*"))
    # print(*ps.search_comp_id(6, "id1,id2,hash"))

    # print(*ps.search_comp_ids(4, 3, "*"))

    # ps.modify_comp(4, 3, similar="dfgs")
    # ps.del_one_comp(8, 6)
    # print(*ps.search_comp_all('*'))
    # ps.close()
    pass
