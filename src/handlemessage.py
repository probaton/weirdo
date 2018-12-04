from sing import sing 

def handle_message(user_id, command, input):
    def list_quotes(user_id, input):
        return input

    def invalid_cmd(user_id, input):
        return 'Invalid command'

    switcher = {
        'lq': list_quotes,
        'sing': sing,
    }

    return switcher.get(command, invalid_cmd)(user_id, input)
