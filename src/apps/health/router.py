from fastapi import APIRouter

from src.apps.health.schemas import HealthResponse
from src.apps.health.services import HealthService

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
async def check_health() -> HealthResponse:
    data = HealthService.get_health_status()
    return HealthResponse(**data)
