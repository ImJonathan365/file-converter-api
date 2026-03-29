import os
from typing import Optional

def get_file_extension(filename: str) -> Optional[str]:
    filename = filename.strip()
    ext = os.path.splitext(filename)[1]
    ext = ext.lower().lstrip('.')
    if not ext or len(ext) > 10:
        return None
    return ext
