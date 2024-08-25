import os
import json
from os.path import exists

from core.utils import settings, paths

def init_dirs():
    # Resources
    if not exists(paths.get_resources_path()): 
        os.mkdir(paths.get_resources_path())
        
    # Logs
    if not exists(paths.get_logs_path()):
        os.mkdir(paths.get_logs_path())

    settings.get_main_settings()

def init_services():

    # Controller
    controller_config_path = paths.get_main_path("hub/controller/config.json")

    controller_settings = {
        "baseURL": "",
        "port": 3000,
        "state": "DEVELOPMENT",
        "auth0": {
            "client_secret": "",
            "client_id": "",
            "base_url": "",
            "client_url": ""
        }
    }
    
    if not exists(controller_config_path):
        with open(controller_config_path, "w") as file:
            json.dump(controller_settings, file, indent=4)
    

if __name__ == "__main__":
    init_dirs()
    init_services()
    result = input("Have the settings been all implemented (y/n)\n")
    if result == "y":
        from core.modules import services
        services.run_services_operation("start")