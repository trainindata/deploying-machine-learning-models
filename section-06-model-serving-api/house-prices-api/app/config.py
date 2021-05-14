import logging
import sys
from typing import List

from loguru import logger
from pydantic import AnyHttpUrl, BaseSettings


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO  # logging levels are ints


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # Meta
    logging: LoggingSettings = LoggingSettings()

    # BACKEND_CORS_ORIGINS is a comma-separated list of origins
    # e.g: http://localhost,http://localhost:4200,http://localhost:3000
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",  # type: ignore
        "http://localhost:8000",  # type: ignore
        "https://localhost:3000",  # type: ignore
        "https://localhost:8000",  # type: ignore
    ]

    PROJECT_NAME: str = "House Price Prediction API"

    class Config:
        case_sensitive = True


def setup_app_logging(config: Settings) -> None:
    """Prepare custom logging for our application."""
    LOGGERS = ("uvicorn.asgi", "uvicorn.access")
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)

    logger.configure(
        handlers=[{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL}]
    )


settings = Settings()
