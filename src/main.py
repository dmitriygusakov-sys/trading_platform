from fastapi import FastAPI

from src.apps.health.router import router as health_router
from src.apps.users.router import router as users_router
from src.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(health_router)
app.include_router(health_router, prefix=settings.API_V1_STR)
app.include_router(users_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root() -> dict:
    return {
        "message": f"Welcome to {settings.PROJECT_NAME} API",
        "docs": "/docs",
    }
