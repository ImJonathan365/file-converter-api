from fastapi import HTTPException, APIRouter
from fastapi.responses import FileResponse
from app.config.settings import settings
import os

router = APIRouter()

@router.get("/{filename}")
async def download_file(filename: str):
    output_dir = os.path.abspath(settings.output_dir)
    file_path = os.path.join(output_dir, filename)

    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/octet-stream"
    )