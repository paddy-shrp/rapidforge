from fastapi import APIRouter

from forge_core.modules import services

router = APIRouter()

@router.get("/is_running")
async def get_status_all():
    return services.get_services_is_running()

@router.put("/{service}/{op}")
async def get_service_status(service: str, op: str):
    return services.run_service_operation(service, op)

@router.get("/{service}/is_running")
async def get_service_is_running(service: str):
    return services.is_running(service)

@router.get("/{service}/is_failed")
async def get_service_is_failed(service: str):
    return services.is_failed(service)

@router.get("/{service}/status")
async def get_service_is_running(service: str):
    return services.get_status(service)

@router.get("/{service}/journal")
async def get_service_is_running(service: str):
    return services.get_journal_last_minute(service)