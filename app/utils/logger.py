import logging
import sys
from app.config.settings import settings

def get_logger(name: str = "file_converter"):
    """
    Get a configured logger instance for the application.
    Args:        name (str): The name of the logger (default: 'file_converter').
    Returns:        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    level = getattr(settings, "log_level", "INFO").upper()
    if level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        level = "INFO"
    logger.setLevel(getattr(logging, level))
    return logger

logger = get_logger()