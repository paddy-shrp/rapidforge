import os
from os.path import exists

from core.modules import services
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

    # Controller Env
    controller_env_path = paths.get_main_path("systemd/controller_service/.env")

    if not exists(controller_env_path):
        with open(controller_env_path, "w") as file:
            file.write('STATE="PRODUCTION"\n')
            file.write('AUTH_CLIENT_URL=""\n')
            file.write('AUTH_CLIENT_ID=""\n')
            file.write('AUTH_CLIENT_SECRET=""\n')
            file.write('PORT=3000\n')

if __name__ == "__main__":
    init_dirs()
    init_services()
    result = input("Have the settings been all implemented (y/n)\n")
    if result == "y":
        services.run_services_operation("start")