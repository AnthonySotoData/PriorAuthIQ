from fastapi import FastAPI

from src.api.policy_search import router as policy_search_router
from src.api.policy_upload import router as policy_upload_router
from src.config import settings


app = FastAPI(
    title=settings.app_name,
    description="AI-powered prior authorization intelligence platform.",
    version=settings.version,
)

# API Routers
app.include_router(policy_search_router)
app.include_router(policy_upload_router)


@app.get("/")
def root() -> dict[str, str]:
    """
    Root endpoint providing basic application information.
    """
    return {
        "name": settings.app_name,
        "status": "running",
        "version": settings.version,
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    """
    Health check endpoint.
    """
    return {
        "status": "healthy",
    }