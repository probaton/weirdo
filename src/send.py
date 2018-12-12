from slackclient import SlackClient
import os

sc = SlackClient(os.environ['SLACK_API_TOKEN'])

sc.api_call("chat.postMessage", channel="general", text="Hello World!")