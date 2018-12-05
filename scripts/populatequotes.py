import os
import sys

sys.path.append('src')
from dbmanager import Db

db = Db()
quote_db = db.quote_table
quote_db.purge()

path = 'db/quotes/'
quotes = []
count = 1
for file_name in os.listdir(path):
    with open(path + file_name) as f:
        quotes.append({ 'id': count, 'quote': f.read() })
        count += 1

quote_db.insert(quotes)
print(f'{quote_db.length} quotes added')
