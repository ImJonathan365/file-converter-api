from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List, Dict

class Settings(BaseSettings):
    app_name: str = Field("File Converter API", env="APP_NAME")
    app_description: str = Field("A file conversion REST API built with FastAPI. Supports converting DOCX, XLSX, PDF, images, and text files into multiple formats.", env="APP_DESCRIPTION")
    app_version: str = Field("1.0.0", env="APP_VERSION")
    api_prefix: str = Field("/api", env="API_PREFIX")
    environment: str = Field("development", env="ENVIRONMENT")
    log_level: str = Field("INFO", env="LOG_LEVEL")
    temp_dir: str = Field("./temp", env="TEMP_DIR")
    output_dir: str = Field("./output", env="OUTPUT_DIR")
    max_file_size_mb: int = Field(20, env="MAX_FILE_SIZE_MB")
    conversion_timeout_seconds: int = Field(120, env="CONVERSION_TIMEOUT_SECONDS")
    allowed_extensions: List[str] = Field(
        default_factory=lambda: [
            "pdf", "docx", "odt", "txt", "md", "html", "xlsx", "csv", "json", "jpg", "jpeg", "png", "bmp", "tiff"
        ],
        env="ALLOWED_EXTENSIONS"
    )
    allowed_mime_types: List[str] = Field(
        default_factory=lambda: [
            "application/pdf",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "text/plain",
            "text/markdown",
            "text/html",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "application/vnd.ms-excel",
            "text/csv",
            "application/json",
            "image/jpeg",
            "image/png",
            "image/bmp",
            "image/tiff"
        ],
        env="ALLOWED_MIME_TYPES"
    )
    
    supported_conversions: Dict[str, List[str]] = {
        "docx": ["pdf", "txt", "html", "md"],
        "odt": ["docx"],
        "txt": ["pdf"],
        "md": ["pdf"],
        "xlsx": ["csv", "json", "txt"],
        "csv": ["xlsx"],
        "pdf": ["docx"],
        "jpg": ["pdf"],
        "jpeg": ["pdf"],
        "png": ["pdf"],
        "bmp": ["pdf"],
        "tiff": ["pdf"]
    }
        
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()