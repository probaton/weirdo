from slackclient import SlackClient
from config import Config

sc = SlackClient(Config().token)

sc.api_call("chat.postMessage", channel="general", text="Hello World!")