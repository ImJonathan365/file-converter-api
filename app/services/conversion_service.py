import os
import uuid
from fastapi import UploadFile
from app.config.paths import get_temp_dir, get_output_dir
from app.converters.dispatcher import get_converter
from app.utils.validators import validate_conversion_request
from app.utils.logger import logger
from app.utils.exceptions import ConversionError
from app.utils.file_manager import ensure_dir, save_upload_file, remove_file, rename_file

class ConversionService:
    @staticmethod
    async def convert(file: UploadFile, target_format: str):
        """
        Convert an uploaded file to the specified target format.

        This method validates the input file and target format, saves the file temporarily,
        performs the conversion using the appropriate converter, and returns the output file path and names.

        Args:
            file (UploadFile): The file to be converted (uploaded by the user).
            target_format (str): The desired output file format (e.g., 'pdf', 'docx').

        Returns:
            tuple: (output_path, output_filename, download_name)
                - output_path (str): Absolute path to the converted file in the output directory.
                - output_filename (str): Unique filename of the converted file.
                - download_name (str): Filename to be used for download (preserves original name).

        Raises:
            ConversionError: If the conversion is not supported or fails.
        """
        validated = await validate_conversion_request(file, target_format)

        filename = validated["filename"]
        input_ext = validated["input_ext"]
        target_ext = validated["target_format"]

        logger.info(f"Starting conversion: {filename} ({input_ext} -> {target_ext})")

        # Get temp and output folders
        temp_dir = get_temp_dir()
        output_dir = get_output_dir()

        ensure_dir(temp_dir)
        ensure_dir(output_dir)

        # Define temporary file path in /temp
        temp_input_filename = f"{uuid.uuid4()}.{input_ext}"
        temp_input_path = os.path.join(temp_dir, temp_input_filename)

        # Reset the file pointer before saving
        await file.seek(0)
        save_upload_file(file, temp_input_path)
        logger.info(f"Temporary file saved at: {temp_input_path}")

        # Define output file name in /output
        original_name = filename.rsplit('.', 1)[0]
        unique_id = str(uuid.uuid4())
        output_filename = f"{unique_id}.{target_ext}"
        output_path = os.path.join(output_dir, output_filename)
        download_name = f"{original_name}.{target_ext}"

        # Find converter
        converter = get_converter(input_ext, target_ext)
        if not converter:
            logger.error(f"No converter found for: {input_ext} -> {target_ext}")
            remove_file(temp_input_path)
            raise ConversionError(f"Conversion from {input_ext} to {target_ext} not supported")

        # Execute converter
        try:
            converter(temp_input_path, output_path)
            logger.info(f"Conversion successful. Output file: {output_path}")
        except Exception as e:
            logger.error(f"Error during conversion: {str(e)}")
            remove_file(temp_input_path)
            raise ConversionError(f"Error during conversion: {str(e)}")

        # Remove temporary file
        remove_file(temp_input_path)
        logger.info(f"Temporary file removed: {temp_input_path}")

        return output_path, output_filename, download_name