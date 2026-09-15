from src.core.config import settings


class HealthService:
    @staticmethod
    def get_health_status() -> dict:
        return {
            "status": "ok",
            "project_name": settings.PROJECT_NAME,
            "debug": settings.DEBUG,
        }
