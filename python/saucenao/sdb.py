import sys
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])
sys.path.append("..")
from simpleToolSql import simpleToolSql

class SDB():
    def __init__(self):
        self.db = simpleToolSql('sdb')

        self.create_tabel()

    def create_tabel(self):
        self.db.execute(
            'create table if not exists PICS (id integer primary key,source text not null, results text);')

    def add(self, pic_data):
        if not self.read(pic_data):
            data = (pic_data['source'], pic_data['results'])
            self.db.execute(
                "insert into PICS (source,results) values (?,?);", data)

    def delet(self, pic_data):
        where = "source='{}'".format(pic_data['source'])
        sql = "delete from PICS where {}".format(where)
        self.db.execute(sql)

    def read(self, pic_data):
        return self.db.query("select * from PICS where source=?;", (pic_data['source'],))

    def read_all(self):
        return self.db.query("select * from PICS;")


if __name__ == "__main__":
    import os
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    # print(os.getcwd())
    picdatas = [{'source': 'asda.jpg', 'results': 'sdfsfsf'},
                {'source': 'sfsaf.jpg', 'results': 'sdfsfsf'},
                ]
    db = SDB()
    print('======add======')
    db.add(picdatas[0])
    db.add(picdatas[1])
    print(db.read_all())
    print('======read======')
    print(db.read(picdatas[1]))
    print(db.read(picdatas[0]))
    print('======delet======')
    db.delet(picdatas[0])
    print(db.read_all())
