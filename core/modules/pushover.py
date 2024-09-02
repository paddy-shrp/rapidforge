import requests

from utils import settings

pushover_set = settings.get_module_settings("pushover", 
                                           {
                                               "user_key": "",
                                               "app_token": ""
                                           })

USER_KEY = pushover_set["user_key"]
TOKEN = pushover_set["app_token"]

def send_notification(message, prio=0):
    payload = {
        "token": TOKEN,
        "user": USER_KEY,
        "message": message,
        "priority": prio
    }
    requests.post("https://api.pushover.net/1/messages.json", data=payload)
