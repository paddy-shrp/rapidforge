from os.path import exists
import json

from utils import paths

MAIN_SETTINGS_PATH = paths.get_settings_path()

def init_settings():
    if not exists(MAIN_SETTINGS_PATH):
        settings = { 
            "timezone": "Europe/Berlin",
            "services": ["forge_controller, forge_dlogger, forge_internal"],
            "mongodb": {
                "uri": "",
                "password": ""
            },
            "pushover": {
                "user_key": "",
                "app_token": "",
            }
        }
        with open(MAIN_SETTINGS_PATH, "w") as file:
            json.dump(settings, file, indent=4)

def get_main_settings():
    if not exists(MAIN_SETTINGS_PATH):
        init_settings()
    return json.load(open(MAIN_SETTINGS_PATH))
