import re
from dbmanager import Db, Query
from random import shuffle
from quotehelpers import int_to_id, reverse_sort_by_id

def search_quotes(user_id, query_str=''):
    if not query_str:
        return 'Missing search parameter'

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
    quotes = reverse_sort_by_id(Db().quote_table.get_all())
    start_id = quote_id or quotes[0]['id']

    result = ''
    count = -1
    for quote in quotes:
        if quote['id'] == start_id:
            count = 10
        if count > 0:
            result += f"{quote['id']} {quote['quote']}\n"
            count -= 1
        if count == 0:
            break
    return result or 'ID not found'

def add_quote(user_id, quote=''):
    if not quote:
        return 'Missing quote'

    quote_table = Db().quote_table
    quotes = reverse_sort_by_id(quote_table.get_all())
    new_id = int_to_id(int(quotes[0]['id']) + 1)
    quote_table.insert({ 'id': new_id, 'quote': quote, 'submitter': user_id })
    return f'Quote {new_id} added' 
