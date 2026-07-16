from fastapi import FastAPI

from src.config import settings

app = FastAPI(
    title=settings.app_name,
    description="AI-powered prior authorization intelligence platform.",
    version=settings.version,
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": settings.app_name,
        "status": "running",
        "version": settings.version,
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}