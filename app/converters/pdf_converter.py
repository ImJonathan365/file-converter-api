import os
import time
from pdf2docx import Converter
from app.utils.exceptions import ConversionEngineError

def pdf_to_docx(input_file: str, output_file: str):
    try:
        cv = Converter(input_file)
        cv.convert(output_file, start=0, end=None)
        cv.close()

        timeout = 10
        start_time = time.time()

        while not os.path.exists(output_file):
            if time.time() - start_time > timeout:
                raise ConversionEngineError("DOCX was not generated")
            time.sleep(0.5)

    except Exception as e:
        raise ConversionEngineError(f"Error converting PDF to DOCX: {str(e)}")