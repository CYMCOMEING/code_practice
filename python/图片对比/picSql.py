import sqlite3
import os

"""
PicData
id, path,source,cosin,similar,hash

CompareData
id1, id2, cosin, similar, hash
"""

class picSql():
    def __init__(self):
        self.filename = "picSql.db"
        self.db = None
        self.c = None

    def open(self):
        self.db = sqlite3.connect(self.filename)
        self.c = self.db.cursor()
        self.create_table()
        return self

    def close(self):
        """
        关闭数据库
        """
        self.c.close()
        self.db.close()
        self.db = None
        self.c = None

    def create_table(self):
        # 判断表头是否存在
        try:
            self.c.execute(
                "create table if not exists PicData (id int primary key, path text not null,source text,cosin  text,"
                "similar  text,hash text);")
            self.c.execute(
                "create table if not exists CompareData (id1 int not null, id2 int not null, cosin text, similar text, hash text);")
        except Exception as e:
            print("create table fail." + str(e))

    def add_pic(self, path):
        try:
            self.c.execute("insert into PicData (path) values (?);", (path,))
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print("add_pic fail." + str(e))
            return False
        return count > 0

    def modify_pic(self, path, key, value):
        keys = ""
        for i in key:
            keys += i + "=?,"
        keys = keys[:-1]
        try:
            # "update PicData set cosin=?,similar=?,hash=? where path=?;"
            sql = "update PicData set " + keys + " where path='" + path + "';"
            self.c.execute(sql, value)
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print("modify_pic fail. \n" + sql + str(e))
            return False
        return count > 0

    def del_pic(self, path):
        try:
            self.c.execute("delete from PicData where path=?", (path,))
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print("del_pic fail." + str(e))
            return False
        return count > 0

    def search_one(self, path, key):
        try:
            # "select * from  PicData where path=?"
            self.c.execute("select " + key + " from  PicData where path=:path", {"path": path})
        except Exception as e:
            print("search_one fail." + str(e))
            return None
        return self.c.fetchall()

    def search_all(self, key):
        try:
            # "select * from PicData"
            self.c.execute("select " + key + " from  PicData")
        except Exception as e:
            print("search_all fail." + str(e))
            return None
        return self.c.fetchall()

    # 支持
    def __enter__(self):
        return self.open()

    def __exit__(self, type, value, trace):
        print(type, value, trace)
        self.close()


if __name__ == "__main__":
    ps = picSql().open()
    ps.add_pic("D:\\dddd.jpg")
    ps.add_pic("D:\\hhhh.jpg")
    ps.add_pic("D:\\yyyy.jpg")
    print(ps.search_all("*"), "\n")
    ps.modify_pic("D:\\hhhh.jpg", ("cosin",), ("SDFAFHSJLDF",))

    ps.modify_pic("D:\\yyyy.jpg", ("cosin", "similar", "hash"), ("SDFALNAGDS", "SFDREGTJYTJ", "LSDHGDKLGJU"))

    print(ps.search_all("*"), "\n")

    ps.del_pic("D:\\hhhh.jpg")
    print(ps.search_all("*"), "\n")

    print(ps.search_all("path"), "\n")
    print(ps.search_all("path, hash"), "\n")

    print(ps.search_one("D:\\yyyy.jpg", "path, similar, hash"), "\n")

    ps.close()
