from fastapi import HTTPException, status
from typing import Optional

def raise_if_error(error: Optional[str], message: str, status_code: int = status.HTTP_400_BAD_REQUEST):
    if error:
        raise HTTPException(
            status_code=status_code,
            detail=message
        )