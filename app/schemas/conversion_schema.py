from pydantic import BaseModel, Field
from typing import Optional

class ConversionRequest(BaseModel):
    target_format: str = Field(..., description="Desired output format, for example: pdf, docx, csv, etc.")

class ConversionResponse(BaseModel):
    filename: str = Field(..., description="Name of the converted file")
    download_url: Optional[str] = Field(None, description="URL to download the converted file")
    message: Optional[str] = Field(None, description="Additional or success message")
