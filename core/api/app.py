from fastapi import FastAPI
from core import settings

app = FastAPI(
    title=settings.project_name,
    openapi_url=settings.api_v1_prefix,
    debug=settings.debug,
)


@app.get("/")
def get_root():
    return {
        "name": settings.project_name,
        "prefix": settings.api_v1_prefix,
        "debug": settings.debug,
    }
