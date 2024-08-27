from os.path import exists
import subprocess
import logging

from utils import settings, paths
from modules import pushover as po

logging.basicConfig(filename=paths.get_logs_path("services.log"), 
                    level=logging.INFO,
                     encoding="utf-8",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S') 

DIR_PATH = "systemd/<name>/commands/"
SERVICES = settings.get_main_settings()["services"]

def get_command_path(service_name, op):
    if service_name in SERVICES:
        return paths.get_main_path(DIR_PATH.replace("<name>", service_name.replace("forge-", "")) + op + ".sh")
    else:
        logging.warning("No service found with the name: " + service_name) 
        return None

def run_services_operation(op):
    for s_name in SERVICES: run_service_operation(s_name, op)

def run_service_operation(service_name, op):
    if op not in ["start", "stop", "restart"]: return False

    running = is_running(service_name)
    
    if op == "start" and running: return False
    if op == "stop" and not running: return False
    
    try:
        path = get_command_path(service_name, op)
        if exists(path):
            subprocess.run(["chmod", "+x", path], check=True)
            process = subprocess.run(path, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        else:
            process = subprocess.run(["sudo", "systemctl", op, service_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        logging.info("Running - " + service_name + " " + op)
        po.send_notification(service_name + " " + op, 0)
        return True
    except:
        logging.error(process.stderr)
        return False
    
def run_command(cmd: list[str]):
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except Exception as e:
        logging.error(e)
        return None

def is_running(service_name):
    result = run_command(['systemctl', 'is-active', service_name])
    if result == None: return False
    return result == "active"
    
def is_failed(service_name):
    result = run_command(['systemctl', 'is-failed', service_name])
    if result == None: return False
    return result == "failed"
    
def get_status(service_name):
    return run_command(["systemctl", "status", service_name])
    
def get_journal_last_minute(service_name):
    return run_command(["journalctl", "-u", service_name, "--since", "1 minute ago", "-q"])

def get_services_is_running():
    if len(SERVICES) == 0: return None
    return {s_name: is_running(s_name) for s_name in SERVICES}

def get_services() -> list[str]:
    return SERVICES