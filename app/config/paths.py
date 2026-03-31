import os
from app.config.settings import settings

def get_temp_dir() -> str:
    """
    Get the absolute path to the temporary directory.
    Returns:
        str: Absolute path to the temp directory.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(base_dir, settings.temp_dir))

def get_output_dir() -> str:
    """
    Get the absolute path to the output directory.
    Returns:
        str: Absolute path to the output directory.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(base_dir, settings.output_dir))
