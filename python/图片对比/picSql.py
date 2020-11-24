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
            self.c.execute("select " + key +
                           " from  PicData where path=:path", {"path": path})
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

    def add_comp(self, **kwargs):
        keys = ""
        values = []
        for kye in kwargs:
            keys += kye + ","
            values.append(kwargs[kye])
        keys = keys[:-1]
        try:
            sql = "insert into CompareData ({}) values ({});".format(
                keys, ','.join(('?'*len(values))))
            self.c.execute(sql, values)
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print("add_comp fail." + str(e))
            return False
        return count > 0

    def modify_comp(self, id1, id2, **kwargs):
        keys = ''
        value = []
        for key in kwargs:
            keys += key + "=?,"
            value.append(kwargs[key])
        keys = keys[:-1]
        try:
            sql = "update CompareData set " + keys + \
                " where (id1=? and id2=?) or (id1=? and id2=?);"
            self.c.execute(sql, value+[id1, id2, id2, id1])
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print("modify_comp fail. \n" + sql + str(e))
            return False
        return count > 0

    def search_comp_id(self, id, key):
        try:
            self.c.execute("select " + key +
                           " from  CompareData where id1=? or id2=?", [id, id])
        except Exception as e:
            print("search_comp_id fail." + str(e))
            return None
        return self.c.fetchall()

    def search_comp_ids(self, id1, id2, key):
        try:
            self.c.execute("select " + key +
                           " from  CompareData where (id1=:id1 and id2=:id2) or (id1=:id2 and id2=:id1);", {'id1': id1, 'id2': id2})
        except Exception as e:
            print("search_comp_ids fail." + str(e))
            return None
        return self.c.fetchall()

    def search_comp_all(self, key):
        try:
            self.c.execute("select " + key +
                           " from  CompareData ;")
        except Exception as e:
            print("search_comp_all fail." + str(e))
            return None
        return self.c.fetchall()

    def del_comp(self, id1, id2):
        try:
            self.c.execute("delete from CompareData where (id1=:id1 and id2=:id2) or (id1=:id2 and id2=:id1);", {
                           'id1': id1, 'id2': id2})
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print("del_comp fail." + str(e))
            return False
        return count > 0

    # 支持with
    def __enter__(self):
        return self.open()

    def __exit__(self, type, value, trace):
        print(type, value, trace)
        self.close()


if __name__ == "__main__":
    ps = picSql().open()
    # ps.add_pic("D:\\dddd.jpg")
    # ps.add_pic("D:\\hhhh.jpg")
    # ps.add_pic("D:\\yyyy.jpg")
    # print(ps.search_all("*"), "\n")
    # ps.modify_pic("D:\\hhhh.jpg", ("cosin",), ("SDFAFHSJLDF",))

    # ps.modify_pic("D:\\yyyy.jpg", ("cosin", "similar", "hash"), ("SDFALNAGDS", "SFDREGTJYTJ", "LSDHGDKLGJU"))

    # print(ps.search_all("*"), "\n")

    # ps.del_pic("D:\\hhhh.jpg")
    # print(ps.search_all("*"), "\n")

    # print(ps.search_all("path"), "\n")
    # print(ps.search_all("path, hash"), "\n")

    # print(ps.search_one("D:\\yyyy.jpg", "path, similar, hash"), "\n")
############
    ps.add_comp(id1=3, id2=4, cosin="sadff", similar="sdffsd", hash="sdfasf")
    ps.add_comp(id1=6, id2=4, cosin="sadff", similar="sdffsd", hash="sdfasf")
    ps.add_comp(id1=6, id2=8, cosin="sadff", similar="sdffsd", hash="sdfasf")

    print(*ps.search_comp_id(4, "*"))
    print(*ps.search_comp_id(6, "id1,id2,hash"))

    print(*ps.search_comp_ids(4, 3, "*"))

    ps.modify_comp(4, 3, similar="dfgs")
    ps.del_comp(8, 6)
    print(*ps.search_comp_all('*'))
    ps.close()
