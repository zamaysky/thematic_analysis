import uvicorn
from fastapi import FastAPI

from config import settings
from routes.themalic_router import router as thematic_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    openapi_url=settings.OPENAPI_URL,
    docs_url=settings.DOCS_URL
)

app.include_router(thematic_router)


if __name__ == '__main__':
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT, debug=True)
