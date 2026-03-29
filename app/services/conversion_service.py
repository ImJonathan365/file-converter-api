import os
import uuid
from fastapi import UploadFile
from app.config.settings import settings
from app.utils.file_utils import get_file_extension
from app.utils.file_validations import validate_filename, validate_file_extension, validate_target_format, validate_conversion_allowed, validate_mime_type, validate_file_size
from app.utils.messages import Messages
from app.utils.error_handler import raise_if_error
from app.converters.dispatcher import get_converter

class ConversionService:
    @staticmethod
    async def validate_and_prepare(file: UploadFile, target_format: str) -> dict:
        filename = os.path.basename(file.filename)
        max_filename_length = 128
    
        reason = validate_filename(filename, max_filename_length)
        raise_if_error(
            reason,
            message=Messages.INVALID_FILENAME.format(reason=reason)
        )

        input_ext = get_file_extension(filename)
        ext_error = validate_file_extension(input_ext, settings.allowed_extensions)
        raise_if_error(
            ext_error,
            message=Messages.FILE_EXTENSION_NOT_ALLOWED.format(ext=ext_error)
        )

        target_format = target_format.lower().strip()
        tgt_error = validate_target_format(target_format, settings.allowed_extensions)
        if tgt_error:
            if tgt_error == Messages.TARGET_FORMAT_NOT_PROVIDED:
                raise_if_error(
                    tgt_error,
                    message=Messages.INVALID_TARGET_FORMAT.format(reason=tgt_error)
                )
            else:
                raise_if_error(
                    tgt_error,
                    message=Messages.OUTPUT_FORMAT_NOT_ALLOWED.format(ext=tgt_error)
                )

        conv_error = validate_conversion_allowed(input_ext, target_format, settings.supported_conversions)
        if conv_error:
            src, tgt = conv_error.split("|")
            raise_if_error(
                conv_error,
                message=Messages.CONVERSION_NOT_ALLOWED.format(src=src, tgt=tgt)
            )

        allowed_mime_types = getattr(settings, "allowed_mime_types", None)
        mime_error = validate_mime_type(file.content_type, allowed_mime_types)
        raise_if_error(
            mime_error,
            message=Messages.MIME_TYPE_NOT_ALLOWED.format(mime=mime_error)
        )

        file.file.seek(0, 2)
        file_size = file.file.tell()
        file.file.seek(0)
        size_error = validate_file_size(file_size, settings.max_file_size_mb)
        if size_error:
            if size_error == "empty":
                raise_if_error(
                    size_error,
                    message=Messages.FILE_EMPTY
                )
            else:
                raise_if_error(
                    size_error,
                    message=Messages.FILE_TOO_LARGE.format(max_mb=size_error)
                )

        await file.seek(0)
        file_size_mb = file_size / (1024 * 1024)
        return {
            "filename": filename,
            "input_ext": input_ext,
            "target_format": target_format,
            "file_size_mb": file_size_mb,
            "content_type": file.content_type
        }
    
    @staticmethod
    async def convert(file: UploadFile, target_format: str):
        # Hacer validaciones

        filename = os.path.basename(file.filename)
        input_ext = get_file_extension(filename)
        target_ext = target_format.lower().strip()

        # Definir carpetas temp y output
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        temp_dir = os.path.join(base_dir, "temp")
        output_dir = os.path.join(base_dir, "output")

        os.makedirs(temp_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        # Guardar archivo original en /temp
        temp_input_filename = f"{uuid.uuid4()}.{input_ext}"
        temp_input_path = os.path.join(temp_dir, temp_input_filename)

        with open(temp_input_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Definir nombre archivo de salida en /output
        original_name = filename.rsplit('.', 1)[0]
        unique_id = str(uuid.uuid4())
        output_filename = f"{unique_id}.{target_ext}"
        output_path = os.path.join(output_dir, output_filename)
        download_name = f"{original_name}.{target_ext}"

        # Buscar converter
        converter = get_converter(input_ext, target_ext)
        if not converter:
            os.remove(temp_input_path)
            raise Exception(f"Conversion from {input_ext} to {target_ext} not supported")

        # Ejecutar converter
        try:
            converter(temp_input_path, output_path)
        except Exception as e:
            os.remove(temp_input_path)
            raise Exception(f"Error during conversion: {str(e)}")

        # Borrar archivo temporal
        os.remove(temp_input_path)

        # Retornar archivo generado
        return output_path, output_filename, download_name