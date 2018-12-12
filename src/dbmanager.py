from tinydb import TinyDB, Query
import os

class Db():
    def __init__(self):
        if not os.environ['DB_PATH']:
            raise Exception('Environment variable DB_PATH not set')
        self.__db = TinyDB(os.environ['DB_PATH'])

    def get_table(self, table_name):
        return Table(self.__db, table_name)

    @property
    def quote_table(self):
        return self.get_table('quote')

    @property
    def sing_table(self):
        return self.get_table('sing')

    @property
    def user_table(self):
        return self.get_table('user')

class Table():
    def __init__(self, db, table_name):
        self.__db = db
        self.__table_name = table_name
        self.__table = db.table(table_name)

    @property
    def length(self):
        return len(self.__table)

    def get(self, query):
        return self.__table.get(query)

    def get_all(self):
        return self.__table.all()

    def search(self, query):
        return self.__table.search(query)

    def insert(self, input):
        if isinstance(input, list):
            self.__table.insert_multiple(input)
        else:
            self.__table.insert(input)

    def update(self, value, query):
        self.__table.update(value, query)

    def purge(self):
        self.__db.purge_table(self.__table_name)
