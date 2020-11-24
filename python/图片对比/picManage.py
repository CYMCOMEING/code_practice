

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


class PicManager(picSql):
    def __init__(self):
        super().__init__()
        self.open()

    def __del__(self):
        self.close()
        print("有释放了")

    def add_pic(self, path):
        if self.search_one(path, "path"):
            print("文件已经存在")
            return
        super().add_pic(path)

    def add_comp(self, **kwargs):
        id1 = kwargs["id1"]
        id2 = kwargs["id2"]
        if self.search_comp_ids(id1, id2, "*"):
            print("id组合已经存在")
            return
        super().add_comp(**kwargs)
        


if __name__ == "__main__":
    pm = PicManager()
    pm.add_pic(r"D:\dddd.jpg")
    pm.add_pic(r"D:\hhhh.jpg")
    pm.add_pic(r"D:\yyyy.jpg")
    print(pm.search_all("*"), "\n")
    pm.modify_pic("D:\\hhhh.jpg", ("cosin",), ("SDFAFHSJLDF",))

    pm.modify_pic("D:\\yyyy.jpg", ("cosin", "similar", "hash"),
                  ("SDFALNAGDS", "SFDREGTJYTJ", "LSDHGDKLGJU"))

    print(pm.search_all("*"), "\n")

    pm.del_pic("D:\\hhhh.jpg")
    print(pm.search_all("*"), "\n")

    print(pm.search_all("path"), "\n")
    print(pm.search_all("path, hash"), "\n")

    print(pm.search_one("D:\\yyyy.jpg", "path, similar, hash"), "\n")

