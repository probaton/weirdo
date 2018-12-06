import re
from operator import itemgetter
from dbmanager import Db, Query

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
