import time
import os
import logging
from slackclient import SlackClient

import logs
from handlemessage import handle_message

def is_request(item):
    return ('type' in item) and ('subtype' not in item) and (item['type'] == 'message')

def parse_command_and_input(text):
    if ' ' in text:
        split_index = text.index(' ')
        return text[0:split_index], text[split_index+1:]
    else:
        return text.strip(), None

def send_response(request):
    command, input = parse_command_and_input(request['text'])
    response = handle_message(request['user'], command, input)
    sc.rtm_send_message(channel=request['channel'], message=response)

logs.config_logging()

if not os.environ['SLACK_API_TOKEN']:
    raise Exception('Environment variable SLACK_API_TOKEN not set')
sc = SlackClient(os.environ['SLACK_API_TOKEN'])

if sc.rtm_connect():
    print('Connection established')
    while sc.server.connected is True:
        start = time.time()
        for item in sc.rtm_read():
            if is_request(item):
                logging.debug('Incoming request: %s', item)
                send_response(item)
        duration = time.time() - start
        if duration < 1:
            time.sleep(1-duration)
else:
    print('Failed to establish a connection')
