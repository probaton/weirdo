from sing import sing 
from quotes import list_quotes, search_quotes, add_quote

def handle_message(user_id, command, input):
    def invalid_cmd(user_id, input):
        return 'Invalid command'

    switcher = {
        'lq': list_quotes,
        'sq': search_quotes,
        'aq': add_quote,
        'sing': sing,
    }

    return switcher.get(command, invalid_cmd)(user_id, input)
