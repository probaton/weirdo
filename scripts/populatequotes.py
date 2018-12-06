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
files = sorted(list(map(lambda x: int(x), os.listdir(path))))
for file_name in files:
    with open(path + str(file_name)) as f:
        quotes.append({ 'id': count, 'quote': f.read(), 'old_id': file_name })
        count += 1

quote_db.insert(quotes)
print(f'{quote_db.length} quotes added')
