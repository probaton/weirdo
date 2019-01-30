from tinydb import TinyDB, Query
import boto3
import os

class Db():
    def __init__(self):
        self.file_name = os.environ['DB_PATH']
        if os.environ['WEIRDO_ENV'] == 'S3':
            self.bucket = boto3.resource('s3').Bucket(os.environ['S3_BUCKET'])
            if not os.path.isfile(self.file_name):
                self.bucket.download_file(self.file_name, self.file_name)
        self.db = TinyDB(self.file_name)

    def get_table(self, table_name):
        return Table(self, table_name)

    @property
    def quote_table(self):
        return self.get_table('quote')

    @property
    def sing_table(self):
        return self.get_table('sing')

    @property
    def user_table(self):
        return self.get_table('user')

    def upload_to_s3(self):
        if os.environ['WEIRDO_ENV'] == 'S3':
            self.bucket.upload_file(self.file_name, self.file_name)

class Table():
    def __init__(self, db_manager, table_name):
        self.__db_manager = db_manager
        self.__table_name = table_name
        self.__table = db_manager.db.table(table_name)

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
        self.__db_manager.upload_to_s3()

    def update(self, value, query):
        self.__table.update(value, query)
        self.__db_manager.upload_to_s3()

    def purge(self):
        self.__db_manager.db.purge_table(self.__table_name)
