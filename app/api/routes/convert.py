from fastapi import APIRouter, UploadFile, File, Form
from app.schemas.conversion_schema import ConversionResponse
from app.config.settings import settings
from app.services.conversion_service import ConversionService

router = APIRouter()

@router.post("/", response_model=ConversionResponse, tags=["convert"])
async def convert_file(
    file: UploadFile = File(..., description="File to be converted"),
    target_format: str = Form(..., description="Desired output format, for example: pdf, docx, csv, etc.")
):
    output_path, stored_filename, download_name = await ConversionService.convert(file, target_format)

    return ConversionResponse(
        filename=download_name,
        download_url=f"{settings.api_prefix}/download/{stored_filename}",
        message="File converted successfully"
    )