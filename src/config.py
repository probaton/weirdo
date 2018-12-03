import json

def get_token():
    with open("my.conf.json") as f:
        json_data = json.load(f)
    return json_data["slack-api-token"]
