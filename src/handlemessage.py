from sing import sing 
from quotes import list_quotes

def handle_message(user_id, command, input):
    def invalid_cmd(user_id, input):
        return 'Invalid command'

    switcher = {
        'lq': list_quotes,
        'sing': sing,
    }

    return switcher.get(command, invalid_cmd)(user_id, input)
