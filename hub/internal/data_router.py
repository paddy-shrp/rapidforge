from fastapi import APIRouter

from core.modules import data

router = APIRouter()

@router.get("/system_info")
async def get_system_info():
    return data.get_slim_system_info()

@router.get("/cpu")
async def get_cpu_info():
    return data.get_cpu_info()

@router.get("/memory")
async def get_memory_info():
    return data.get_memory_info()

@router.get("/disk")
async def get_disk_info():
    return data.get_disk_info()

@router.get("/system_history")
async def get_system_history():
    return data.get_system_history()