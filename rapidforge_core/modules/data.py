import psutil

def get_cpu_info():
    cpu_info_dic = {
        "count": psutil.cpu_count(logical=True),
        "usage": psutil.cpu_percent(interval=1)
    }
    return cpu_info_dic

def get_memory_info():
    memory_info = psutil.virtual_memory()
    memory_info_dic = {
        "total": memory_info.total,
        "used": memory_info.used,
        "available": memory_info.available,
        "usage": memory_info.percent
    }
    return memory_info_dic

def get_disk_info():
    disk_info = psutil.disk_usage('/')
    disk_info_dic = {
        "total": disk_info.total,
        "used": disk_info.used,
        "available": disk_info.free,
        "usage": disk_info.percent
    }
    return disk_info_dic

def get_system_info():
    system_info = {
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info()
    }
    return system_info

def get_slim_system_info():
    slim_system_info = {
        "cpu": get_cpu_info()["usage"],
        "memory": get_memory_info()["usage"],
        "disk": get_disk_info()["usage"]
    }
    return slim_system_info