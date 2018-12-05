import json

class Config():
    def __init__(self):
        with open("my.conf.json") as f:
            self.config = json.load(f)

    @property
    def token(self):
        return self.config["slack-api-token"]

    @property
    def db_path(self):
        return self.config["db-path"]
