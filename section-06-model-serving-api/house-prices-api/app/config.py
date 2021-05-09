import json
import logging
import pathlib
import sys
from loguru import logger
from pydantic import (
    AnyHttpUrl,
    BaseSettings,
)
from typing import Any, List, Mapping, Optional

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent


def _list_parse_fallback(v: Any) -> Any:
    try:
        return json.loads(v)
    except Exception:
        return v.split(",")


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO  # logging levels are ints


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # Meta
    logging: LoggingSettings = LoggingSettings()

    DOMAIN: str = "localhost:8001"
    SERVER_HOST: AnyHttpUrl = "http://localhost:8001"  # type: ignore

    # BACKEND_CORS_ORIGINS is a comma-separated list of origins
    # e.g: http://localhost,http://localhost:4200,http://localhost:3000
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",  # type: ignore
        "http://localhost:8000",  # type: ignore
        "https://localhost:3000",  # type: ignore
        "https://localhost:8000",  # type: ignore
    ]
    # Origins that match this regex OR are in the above list are allowed
    BACKEND_CORS_ORIGIN_REGEX: Optional[
        str
    ] = "https.*\.(netlify.app)"  # noqa: W605

    PROJECT_NAME: str = "House Price Prediction API"

    class Config:
        case_sensitive = True
        json_loads = _list_parse_fallback


def setup_app_logging(config: Settings) -> None:
    """Prepare custom logging for our application."""
    LOGGERS = ("uvicorn.asgi", "uvicorn.access")
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)

    logger.configure(
        handlers=[{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL}]
    )


settings = Settings()
