import time
from slackclient import SlackClient

from config import Config
from handlemessage import handle_message

sc = SlackClient(Config().token)
if sc.rtm_connect():
    print('Connection established')
    while sc.server.connected is True:
        start = time.time()
        for item in sc.rtm_read():
            if 'type' in item and item['type'] == 'message':
                print(item)
                text = item['text']
                if ' ' in text:
                    split_index = text.index(' ')
                    command = text[0:split_index]
                    input = text[split_index+1:]
                else:
                    command = text.strip()
                    input = None
                sc.rtm_send_message(channel=item['channel'], message=handle_message(item['user'], command, input))
        duration = time.time() - start
        if duration < 1:
            time.sleep(1-duration)
else:
    print('Failed to establish a connection')
