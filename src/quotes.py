import re
from operator import itemgetter
from dbmanager import Db, Query
from random import shuffle

def search_quotes(user_id, query_str):
    query = Query().quote.search(query_str, flags=re.IGNORECASE)
    quote_table = Db().quote_table

    id_list = list(map(lambda x: x['id'], quote_table.search(query)))
    if len(id_list) == 0:
        return 'No matches found'

    shuffle(id_list)

    result = ''
    for id in id_list[:3]:
        result += f"{id} {quote_table.get(Query().id == id)['quote']}\n"
    return result

def list_quotes(user_id, quote_id=None):
    quote_table = Db().quote_table
    quotes = sorted(quote_table.get_all(), key=itemgetter('id'), reverse=True)

    quote_id = int(quote_id) if quote_id else quotes[0]['id']
    result = ''
    count = -1
    for quote in quotes:
        if quote['id'] == quote_id:
            count = 10
        if count > 0:
            result += f"{quote['id']} {quote['quote']}\n"
            count -= 1
        if count == 0:
            break
    return result
