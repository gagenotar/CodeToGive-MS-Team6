import json

class Config:
    def __init__(self):
        with open('app\email_module\email_config.json') as config_file:
            config_data = json.load(config_file)
            self.EMAIL_FROM = config_data['email_from']
            self.CLIENT_SECRET_FILE = config_data['client_secret_file']
            self.SCOPES = config_data['scopes']

config = Config()
