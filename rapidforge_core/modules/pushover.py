import requests

from utils import settings

pushover_set = settings.get_main_settings()["pushover"]

TOKEN = pushover_set["token"]
USER_KEY = pushover_set["user_key"]

def send_notification(message, prio=0):
    payload = {
        "token": TOKEN,
        "user": USER_KEY,
        "message": message,
        "priority": prio
    }
    requests.post("https://api.pushover.net/1/messages.json", data=payload)
