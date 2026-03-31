from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.api.routes.convert import router as convert_router
from app.api.routes.health import router as health_router
from app.api.routes.formats import router as formats_router
from app.api.routes.download import router as download_router
from app.utils.logger import logger
from app.utils.exceptions import ConversionError, ValidationError
from fastapi.responses import JSONResponse

def create_app() -> FastAPI:

    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.app_version,
        docs_url=f"{settings.api_prefix}/docs",
        redoc_url=f"{settings.api_prefix}/redoc",
    )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled Exception: {str(exc)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal server error. Please try again later.",
                "type": "internal_error"
            }
        )

    @app.exception_handler(ConversionError)
    async def conversion_error_handler(request: Request, exc: ConversionError):
        logger.error(f"ConversionError: {exc.message}")
        return JSONResponse(
            status_code=500,
            content={"detail": exc.message, "type": "conversion_error"}
        )

    @app.exception_handler(ValidationError)
    async def validation_error_handler(request: Request, exc: ValidationError):
        logger.error(f"ValidationError: {exc.message}")
        return JSONResponse(
            status_code=400,
            content={"detail": exc.message, "type": "validation_error"}
        )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(convert_router, prefix=f"{settings.api_prefix}/convert", tags=["convert"])
    app.include_router(health_router, prefix=f"{settings.api_prefix}/health", tags=["health"])
    app.include_router(formats_router, prefix=f"{settings.api_prefix}/formats", tags=["formats"])
    app.include_router(download_router, prefix=f"{settings.api_prefix}/download", tags=["download"])
    return app

app = create_app()