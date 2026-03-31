import os
from typing import Optional

def get_file_extension(filename: str) -> Optional[str]:
    """
    Extract and return the file extension from a filename.
    Args:
        filename (str): The name of the file from which to extract the extension.
    Returns:
        Optional[str]: The file extension in lowercase without the dot, or None if invalid.
    """
    filename = filename.strip()
    ext = os.path.splitext(filename)[1]
    ext = ext.lower().lstrip('.')
    if not ext or len(ext) > 10:
        return None
    return ext
