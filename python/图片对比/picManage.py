

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
        if os.path.exists(path) and self.search("id", "path=?", [path,]):
            ahash_data = ahash(path)
            dhash_data = dhash(path)
            self.modify_pic("ahash=?,dhash=?", "path=?", [
                            ahash_data, dhash_data, path])

    def generater_all(self):
        files = self.search("path", "ahash is '' or dhash is ''")
        for file in files:
            if os.path.exists(file):
                ahash_data = ahash(file)
                dhash_data = dhash(file)
                self.modify_pic("ahash=?,dhash=?", "path=?", [
                    ahash_data, dhash_data, file])

    def comp_id(self, id1, id2):
        pic1 = self.query(
            "select id,path,ahash,dhash from  PicData where id=?;", id1)
        pic2 = self.query(
            "select id,path,ahash,dhash from  PicData where id=?;", id2)
        if (not pic1) and (not pic2):
            print("id不在数据库 ")
            return
        pic1 = pic1[0]
        pic2 = pic2[0]
        if pic1[2] is None or pic1[3] is None:
            self.generate_hash(pic1[1])
        if pic2[2] is None or pic2[3] is None:
            self.generate_hash(pic2[1])
        comp_ahash = campHash(pic1[2], pic2[2])
        comp_dhash = campHash(pic1[3], pic2[3])
        value = [id1, id2]
        res = self.execute(
            "select id1,id2 from  PicData where (id1=:id1 and id2=:id2) or (id1=:id2 and id2=:id1);", {"id1": id1, "id2":id2})
        if res:
            value = [res[0][0], res[0][1]]
        value.append(comp_ahash)
        value.append(comp_dhash)
        self.execute(
            "insert or replace into CompareData (id1,id2,ahash, dhash) values (?,?,?,?);", value)
        
    def copm_search(self, id1, id2=None):
        value = [id1]
        if id2 is None:
            where = "id1=:id1 or id2=:id1"
        else:
            where = "(id1=:id1 and id2=:id2) or (id1=:id2 and id2=:id1)"
            value.append(id2)
        sql = "select id1,id2,ahash,dhash CompareData  PicData where {};".format(where)
        return self.query(sql, value)


def get_files(dir):
    files = []
    for file in glob.glob(dir):
        if os.path.isfile(file):
            files.append(os.path.abspath(file))
    return files


def show(data):
    if not data:
        return
    for item in data:
        line = ""
        for index in item:
            line += str(index) + "\t"
        print(line)


if __name__ == "__main__":
    # 添加图片，多张
    # 显示
    # 删除
    # 修改
    # 生成hash，批量
    # 对比某个图片
    # 对比记录排序
    pm = PicManager()
    pm.add_pics(get_files("*[.jpg .png]"))
    show(pm.search('*'))
    # show(pm.search("id,path", "ahash is '' and dhash is ''"))
    # pm.del_pic("id=?", [1])
    # pm.modify_pic("ahash=?,shash=?", "id=?", ["sdff", "sdff", "2"])
    
