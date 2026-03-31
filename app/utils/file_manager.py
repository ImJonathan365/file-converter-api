import os
from fastapi import UploadFile
from app.utils.logger import logger
import time

def remove_old_files_in_dir(directory: str, max_age_seconds: int = 3600):
    """
    Remove files older than max_age_seconds in the specified directory.
    """
    now = time.time()
    if not os.path.exists(directory):
        return
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                file_age = now - os.path.getmtime(file_path)
                if file_age > max_age_seconds:
                    os.remove(file_path)
                    logger.info(f"Removed old file: {file_path}")
        except Exception as e:
            logger.warning(f"Could not remove file {file_path}: {str(e)}")

def ensure_dir(path: str):
    """
    Ensure that a directory exists at the given path. If it does not exist, it will be created.
    """
    os.makedirs(path, exist_ok=True)

def save_upload_file(upload_file: UploadFile, destination: str):
    """
    Save an uploaded file to the specified destination path.
    """
    with open(destination, "wb") as buffer:
        content = upload_file.file.read()
        buffer.write(content)
    logger.info(f"File saved at: {destination}")

def remove_file(path: str):
    """
    Remove a file at the given path if it exists.
    """
    try:
        os.remove(path)
        logger.info(f"File removed: {path}")
    except FileNotFoundError:
        logger.warning(f"Attempted to remove non-existent file: {path}")
    except Exception as e:
        logger.error(f"Error removing file {path}: {str(e)}")

def rename_file(src: str, dst: str):
    """
    Rename or move a file from src to dst.
    """
    os.rename(src, dst)
    logger.info(f"File renamed/moved from {src} to {dst}")