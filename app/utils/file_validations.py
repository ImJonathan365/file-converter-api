from typing import Optional
from app.utils.messages import Messages

def validate_filename(filename: str, max_length: int) -> Optional[str]:
    if not filename or len(filename) > max_length:
        return Messages.FILE_NAME_INVALID
    if ".." in filename or filename.startswith(('/', '\\')):
        return Messages.FILE_NAME_WITH_INVALID_PATH
    return None

def validate_file_extension(input_ext: str, allowed_extensions: list) -> Optional[str]:
    if not input_ext or input_ext not in allowed_extensions:
        return input_ext
    return None

def validate_target_format(target_format: str, allowed_extensions: list) -> Optional[str]:
    if not target_format:
        return Messages.TARGET_FORMAT_NOT_PROVIDED
    if not target_format.isalpha() or target_format not in allowed_extensions:
        return target_format
    return None

def validate_conversion_allowed(input_ext: str, target_format: str, supported_conversions: dict) -> Optional[str]:
    allowed_targets = supported_conversions.get(input_ext, [])
    if target_format not in allowed_targets:
        return f"{input_ext}|{target_format}"
    return None

def validate_file_size(file_size: int, max_file_size_mb: int) -> Optional[str]:
    file_size_mb = file_size / (1024 * 1024)
    if file_size_mb > max_file_size_mb:
        return str(max_file_size_mb)
    if file_size == 0:
        return "empty"
    return None

def validate_mime_type(content_type: str, allowed_mime_types: list) -> Optional[str]:
    if allowed_mime_types and content_type not in allowed_mime_types:
        return content_type
    return None
