import sqlite3

class DBHelper:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "create table if not exists items"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self,item_text):
        stmt = "insert into items values"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()
    
    def get_items(self):
        stmt = "select description items from items"
        return [x[0] for x in self.conn.execute(stmt)]
    
    