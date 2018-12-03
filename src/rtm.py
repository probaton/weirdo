from slackclient import SlackClient
from config import get_token
import time

def message_handler(command, input, channel):
    def list_quotes(query, channel):
        sc.rtm_send_message(channel=channel, message=query)

    def invalid_cmd(input, channel):
        sc.rtm_send_message(channel=channel, message='Invalid command')

    switcher = {
        'lq': list_quotes
    }

    handler_function = switcher.get(command, invalid_cmd)
    handler_function(input, channel)

sc = SlackClient(get_token())
if sc.rtm_connect():
    print('Connection established')
    while sc.server.connected is True:
        commands = []
        for item in sc.rtm_read():
            if 'text' in item and 'ok' not in item:
                text = item['text']
                split_index = text.index(' ')
                commands.append({ 'command': text[0:split_index], 'input': text[split_index+1:], 'channel': item['channel'] })

        for cmd in commands:
            message_handler(cmd['command'], cmd['input'], cmd['channel'])
        time.sleep(1)
else:
    print('Failed to establish a connection')
