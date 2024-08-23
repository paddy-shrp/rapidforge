from os.path import join, abspath, dirname
    
def get_path(file):
    return dirname(abspath(file)) + "/"

def get_main_path(file_path=""):
    return join(dirname(dirname(dirname(abspath(__file__)))), file_path)

def get_resources_path(file_path=""):
    return get_main_path(join("resources", file_path))

def get_settings_path():
    return get_resources_path("settings.json")

def get_credentials_path():
    return get_resources_path("credentials/")

def get_logs_path(file_path=""):
    return get_resources_path(join("logs", file_path))