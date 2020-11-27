import sqlite3
import os

"""
PicData
id, path,source,cosin,similar, ahash, dhash

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
                "create table if not exists PicData (id integer primary key autoincrement, path text not null,source text,cosin  text,"
                "similar  text, ahash text, dhash text);")
            self.c.execute(
                "create table if not exists CompareData (id1 int not null, id2 int not null, cosin text, similar text, ahash text, dhash text);")
        except Exception as e:
            print("create table fail. " + str(e))

    def modify_pic(self, where, **kwargs):
        keys = ""
        value = []
        for key in kwargs:
            keys += key + "=?,"
            value.append(kwargs[key])
        keys = keys[:-1]
        value.append(where[1])
        try:
            # "update PicData set cosin=?,similar=?,hash=? where path=?;"
            sql = "update PicData set {} where {}=?;".format(
                keys, where[0])
            self.c.execute(sql, value)
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print("modify_pic fail. \n" + sql + str(e))
            return False
        return count > 0

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
            print("add_comp fail. " + str(e))
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
            print("search_comp_id fail. " + str(e))
            return None
        return self.c.fetchall()

    def search_comp_ids(self, id1, id2, key):
        try:
            self.c.execute("select " + key +
                           " from  CompareData where (id1=:id1 and id2=:id2) or (id1=:id2 and id2=:id1);", {'id1': id1, 'id2': id2})
        except Exception as e:
            print("search_comp_ids fail. " + str(e))
            return None
        return self.c.fetchall()

    def search_comp_all(self, key):
        try:
            self.c.execute("select " + key +
                           " from  CompareData ;")
        except Exception as e:
            print("search_comp_all fail. " + str(e))
            return None
        return self.c.fetchall()

    def del_one_comp(self, id1, id2):
        try:
            self.c.execute("delete from CompareData where (id1=:id1 and id2=:id2) or (id1=:id2 and id2=:id1);", {
                           'id1': id1, 'id2': id2})
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print("del_one_comp fail. " + str(e))
            return False
        return count > 0

    def del_all_comp(self, id):
        try:
            self.c.execute(
                "delete from CompareData where id1=:id or id2=:id;", {'id': id})
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print("del_all_comp fail. " + str(e))
            return False
        return count > 0

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
        if param is None:
            self.c.execute(sql)
        else:
            self.c.execute(sql, param)
        return self.c.fetchall()

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
