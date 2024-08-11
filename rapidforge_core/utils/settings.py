from os.path import exists
import json

from utils import paths

MAIN_SETTINGS_PATH = paths.get_settings_path()

def init_settings():
    if not exists(MAIN_SETTINGS_PATH):
        settings = { 
            "timezone": "Europe/Berlin",
            "services": [],
            "mongodb": {
                "uri": "",
                "username": "",
                "password": ""
            },
            "pushover": {
                "token": "",
                "user_key": ""
            }
        }
        
        with open(MAIN_SETTINGS_PATH, "w") as file:
            json.dump(settings, file, indent=4)

def get_main_settings():
    if not exists(MAIN_SETTINGS_PATH):
        init_settings()
    return json.load(open(MAIN_SETTINGS_PATH))
