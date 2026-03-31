import os
from fastapi import UploadFile
from app.config.settings import settings
from app.utils.file_utils import get_file_extension
from app.utils.file_validations import (
    validate_filename,
    validate_file_extension,
    validate_target_format,
    validate_conversion_allowed,
    validate_mime_type,
    validate_file_size,
)
from app.utils.messages import Messages
from app.utils.logger import logger
from app.utils.exceptions import ValidationError

async def validate_conversion_request(file: UploadFile, target_format: str) -> dict:
    """
    Validate an uploaded file and the requested target format for conversion.

    Checks filename, extension, target format, allowed conversions, MIME type, and file size.
    Raises ValidationError if any check fails.

    Args:
        file (UploadFile): The uploaded file to validate.
        target_format (str): The requested output format.

    Returns:
        dict: Dictionary with validated filename, input_ext, and target_format.
    """

    filename = os.path.basename(file.filename)
    max_filename_length = 128
    logger.info(f"Validating received file: {filename}")

    reason = validate_filename(filename, max_filename_length)
    if reason:
        logger.error(f"Invalid filename: {reason}")
        raise ValidationError(Messages.INVALID_FILENAME.format(reason=reason))

    input_ext = get_file_extension(filename)
    ext_error = validate_file_extension(input_ext, settings.allowed_extensions)
    if ext_error:
        logger.error(f"File extension not allowed: {input_ext}")
        raise ValidationError(Messages.FILE_EXTENSION_NOT_ALLOWED.format(ext=ext_error))

    target_format = target_format.lower().strip()
    tgt_error = validate_target_format(target_format, settings.allowed_extensions)
    if tgt_error:
        if tgt_error == Messages.TARGET_FORMAT_NOT_PROVIDED:
            logger.error("Target format not provided.")
            raise ValidationError(Messages.INVALID_TARGET_FORMAT.format(reason=tgt_error))
        else:
            logger.error(f"Target format not allowed: {target_format}")
            raise ValidationError(Messages.OUTPUT_FORMAT_NOT_ALLOWED.format(ext=tgt_error))

    conv_error = validate_conversion_allowed(input_ext, target_format, settings.supported_conversions)
    if conv_error:
        src, tgt = conv_error.split("|")
        logger.error(f"Conversion not allowed: {src} -> {tgt}")
        raise ValidationError(Messages.CONVERSION_NOT_ALLOWED.format(src=src, tgt=tgt))

    allowed_mime_types = getattr(settings, "allowed_mime_types", None)
    mime_error = validate_mime_type(file.content_type, allowed_mime_types)
    if mime_error:
        logger.error(f"MIME type not allowed: {file.content_type}")
        raise ValidationError(Messages.MIME_TYPE_NOT_ALLOWED.format(mime=mime_error))

    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)
    size_error = validate_file_size(file_size, settings.max_file_size_mb)
    if size_error:
        if size_error == "empty":
            logger.error("File is empty.")
            raise ValidationError(Messages.FILE_EMPTY)
        else:
            logger.error(f"File too large: {file_size} bytes")
            raise ValidationError(Messages.FILE_TOO_LARGE.format(max_mb=size_error))

    await file.seek(0)
    logger.info(f"Validation successful for file: {filename} ({input_ext} -> {target_format})")
    return {
        "filename": filename,
        "input_ext": input_ext,
        "target_format": target_format
    }