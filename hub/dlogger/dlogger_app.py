import time
from threading import Thread
import numpy as np

from core.modules import data, mongodb as mdb, services, pushover as po

def check_service_events():
    for service_name in services.get_services():
        if(services.is_failed(service_name)):
            po.send_notification("ATTENTION " + service_name.upper() + " FAILED!", 1)
    return True

def log_data():
    return data.log_system_history()
    
def format_data():
    FORMAT_INTERVAL_SECONDS = 90
    
    last24hoursTimestamp = time.time() - 24 * 60 * 60
    query = {"timestamp": {"$lt": last24hoursTimestamp}}
    
    mdb.remove_points("SERVER", "INFO", query)
        
    points = mdb.get_points("SERVER", "INFO")
    marker_index = 0

    for i in range(len(points)):
        if(points[i]["timestamp"] - points[marker_index]["timestamp"] > FORMAT_INTERVAL_SECONDS):
            inBetweenPoints = points[marker_index:i]
            
            mdb.update_point("SERVER", "INFO", points[marker_index]["_id"], {
                "cpu": np.mean([p["cpu"] for p in inBetweenPoints]),
                "memory": np.mean([p["memory"] for p in inBetweenPoints]),
                "disk": np.mean([p["disk"] for p in inBetweenPoints])
            })
            
            # Exclude First
            inBetweenPoints = inBetweenPoints[1:]
            
            mdb.remove_points("SERVER", "INFO", {"_id": { "$in": [p["_id"] for p in inBetweenPoints]}})
            marker_index = i
    
    return True 
 
methods = [
    (check_service_events, 10),
    (log_data, 5),
    (format_data, 60)
]

def run_task(method, interval):
    last_run = time.time()
    while True:
        if (time.time() - last_run) > interval:
            if method():
                print(method)
                last_run = time.time()
        time.sleep(1)

def main():
    try:
        threads = []
        for method, interval in methods:
            thread = Thread(target=run_task, args=(method, interval))
            threads.append(thread)
            thread.start()
            
        for thread in threads: 
            thread.join()
        
    except Exception as e:
        print(e) 

if __name__ == "__main__":
    main()
    