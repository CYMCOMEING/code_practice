from simpleToolSql import simpleToolSql

class SDB():
    def __init__(self):
        self.db = simpleToolSql('sdb')

        self.create_tabel()
        self.db.close()

    def create_tabel(self):
        self.db.execute('create table if not exists PICS (id integer primary key,name text not null);')

    def add(self, pic_data):
        if not self.read(pic_data):
            data = (pic_data['name'],)
            self.db.execute("insert into PICS (name) values (?);",data)

    def delet(self, pic_data):
        where = "name='{}'".format(pic_data['name'])
        sql = "delete from PICS where {}".format(where)
        self.db.execute(sql)

    def read(self, pic_data):
        return self.db.query("select * from PICS where name=?;",(pic_data['name'],))

    def read_all(self):
        return self.db.query("select * from PICS;")

    