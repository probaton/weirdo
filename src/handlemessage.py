from sing import sing 
from quotes import list_quotes, search_quotes, add_quote
from time import strftime, localtime 

def handle_message(user_id, command, input=None):
    def invalid_cmd(user_id, input):
        return 'Invalid command'

    switcher = {
        'lq': list_quotes,
        'sq': search_quotes,
        'aq': add_quote,
        'sing': sing,
    }
    try:
        return switcher.get(command, invalid_cmd)(user_id, input)
    except Exception as e:
        print(f"[{strftime('%Y-%m-%d %H:%M:%S', localtime())}] Error while handling {command}: {e}")
        return "Oops, that didn't work" 

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    print(handle_message(*sys.argv[1:]))
