

"""
目的找出重复的图片
1. 添加图片，去重
2. 删除图片，所有表
3. 修改图片，特征码，需要重新管理对比结果
4. 生成特征码
5. 对比特征码，生成对比结果表
6. 搜图
"""
from picSql import picSql
from comperTools import ahash, dhash, campHash
import glob
import os


class PicManager(picSql):
    def __init__(self):
        super().__init__()
        self.open()
        self.create_table("create table if not exists PicData (id integer primary key autoincrement, path text not null unique,remake text,cosin  text,"
                          "similar  text, ahash text, dhash text);")
        self.create_table(
            "create table if not exists CompareData (id1 int not null, id2 int not null, cosin text, similar text, ahash text, dhash text);")

    def __del__(self):
        self.close()

    def add_pic(self, path):
        self.execute(
            "insert or ignore into PicData (path) values (?);", (path,))

    def add_pics(self, paths):
        for path in paths:
            self.add_pic(path)

    def search(self, col, where=None, param=None):
        if where:
            sql = "select {} from  PicData where {};".format(col, where)
        else:
            sql = "select {} from  PicData".format(col)
        return self.query(sql, param)

    def del_pic(self, where, param=None):
        sql = "delete from PicData where {}".format(where)
        self.execute(sql, param)

    def modify_pic(self, col, where, param=None):
        sql = "update PicData set {} where {};".format(col, where)
        self.execute(sql, param)

    def generate_hash(self, path):
        if os.path.exists(path) and self.search("id", "path=?", [path, ]):
            ahash_data = ahash(path)
            dhash_data = dhash(path)
            self.modify_pic("ahash=?,dhash=?", "path=?", (
                            ahash_data, dhash_data, path))

    def generater_all(self):
        files = self.search("path", "ahash is null or dhash is null")
        for file in files:
            if os.path.exists(file[0]):
                ahash_data = ahash(file[0])
                dhash_data = dhash(file[0])
                self.modify_pic("ahash=?,dhash=?", "path=?", (
                    ahash_data, dhash_data, file[0]))

    def comp_id(self, id1, id2):
        pic1 = self.query(
            "select id,path,ahash,dhash from  PicData where id=? and ahash is not null and dhash is not null;", (id1,))
        pic2 = self.query(
            "select id,path,ahash,dhash from  PicData where id=? and ahash is not null and dhash is not null;", (id2,))
        if (not pic1) and (not pic2):
            print("id不存在数据库或hash没数据 ")
            return
        pic1 = pic1[0]
        pic2 = pic2[0]
        if pic1[2] is None or pic1[3] is None:
            self.generate_hash(pic1[1])
        if pic2[2] is None or pic2[3] is None:
            self.generate_hash(pic2[1])
        comp_ahash = campHash(pic1[2], pic2[2])
        comp_dhash = campHash(pic1[3], pic2[3])

        res = self.query(
            "select id1,id2 from CompareData where (id1=:id1 and id2=:id2) or (id1=:id2 and id2=:id1);", {"id1": id1, "id2": id2})
        if res:
            # 已经存在
            sql = "update CompareData set ahash=?, dhash=? where id1=? and id2=? ;"
            value = [comp_ahash, comp_dhash, res[0][0], res[0][1]]
        else:
            # 不存在
            sql = "insert into CompareData (id1,id2,ahash, dhash) values (?,?,?,?);"
            value = [id1, id2, comp_ahash, comp_dhash]
        self.execute(sql, tuple(value))

    def copm_search(self, id1=None, id2=None):
        if id1 is None:
            value = None
            where = ""
        elif id2 is None:
            value = {"id1": id1}
            where = "where id1=:id1 or id2=:id1"
        else:
            where = "where (id1=:id1 and id2=:id2) or (id1=:id2 and id2=:id1)"
            value["id2"] = id2
        sql = "select id1,id2,ahash,dhash from CompareData {};".format(
            where)
        return self.query(sql, value)

    def show(self, data):
        if not data:
            return
        print("\t".join(self.get_cursor_head()))
        for item in data:
            line = ""
            for index in item:
                line += str(index) + "\t"
            print(line)


def get_files(dir):
    files = []
    for file in glob.glob(dir):
        if os.path.isfile(file):
            files.append(os.path.abspath(file))
    return files


if __name__ == "__main__":
    # 添加图片，多张
    # 显示
    # 删除
    # 修改
    # 生成hash，批量
    # 对比某个图片
    # 对比记录排序
    pass
    # pm = PicManager()
    # pm.add_pics(get_files("*[.jpg .png]"))
    # pm.show(pm.search('*'))
    # pm.show(pm.search("id,path,ahash,dhash", "ahash is null or dhash is null"))
    # pm.del_pic("id=?", (1,))
    # pm.modify_pic("ahash=?,dhash=?", "id=?", ("sdff", "sdff", "2"))
    # pm.show(pm.search('*'))

    # pm.generate_hash(r"D:\git\code_practice\python\图片对比\a.jpg")
    # pm.generater_all()
    # pm.show(pm.search('*'))

    # pm.comp_id(1, 2)
    # pm.comp_id(1, 3)
    # pm.comp_id(3, 2)
    # pm.show(pm.search('*'))
    # pm.show(pm.copm_search())
