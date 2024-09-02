from os.path import exists
import json

from utils import paths

MAIN_SETTINGS_PATH = paths.get_settings_path("settings.json")
MODULES_SETTINGS_PATH = paths.get_settings_path("modules.json")

def init_settings():
    if not exists(MAIN_SETTINGS_PATH):
        settings = { 
            "timezone": "Europe/Berlin",
            "services": ["forge_controller", "forge_dlogger", "forge_internal"]
        }
        with open(MAIN_SETTINGS_PATH, "w") as file:
            json.dump(settings, file, indent=4)

    if not exists(MODULES_SETTINGS_PATH):
        with open(MODULES_SETTINGS_PATH, "w") as file: 
            json.dump({}, file)

def get_main_settings():
    if not exists(MAIN_SETTINGS_PATH):
        init_settings()
    return json.load(open(MAIN_SETTINGS_PATH))

def get_module_settings(module_name, default_settings={}):
    if not exists(MODULES_SETTINGS_PATH):
        init_settings()
    
    modules_settings = json.load(open(MODULES_SETTINGS_PATH))

    if module_name in modules_settings:
        return modules_settings[module_name]
    else:
        modules_settings[module_name] = default_settings
        with open(MODULES_SETTINGS_PATH, "w") as file:
            json.dump(modules_settings, file, indent=4)
        return modules_settings[module_name]
