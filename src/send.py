from slackclient import SlackClient
from config import get_token

sc = SlackClient(get_token())

sc.api_call("chat.postMessage", channel="general", text="Hello World!")