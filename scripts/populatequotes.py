import os
from tinydb import TinyDB, Query

db = TinyDB('./db/db.json')
db.purge_table('quote')
quote_db = db.table('quote')

path = 'db/quotes/'
quotes = []
count = 1
for file_name in os.listdir(path):
    with open(path + file_name) as f:
        quotes.append({ 'id': count, 'quote': f.read() })
        count += 1

quote_db.insert_multiple(quotes)
print(f'{len(quote_db)} quotes added')
