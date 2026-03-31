import pandas as pd
import os
import time
from app.utils.exceptions import ConversionEngineError

def xlsx_to_csv(input_file: str, output_file: str):
    try:
        df = pd.read_excel(input_file)
        df.to_csv(output_file, index=False, encoding="utf-8")

        timeout = 10
        start_time = time.time()

        while not os.path.exists(output_file):
            if time.time() - start_time > timeout:
                raise ConversionEngineError("CSV was not generated")
            time.sleep(0.5)

    except Exception as e:
        raise ConversionEngineError(f"Error converting XLSX to CSV: {str(e)}")
    
def xlsx_to_json(input_file: str, output_file: str):
    try:
        df = pd.read_excel(input_file)
        df.to_json(output_file, orient="records", force_ascii=False, indent=4)

        timeout = 10
        start_time = time.time()

        while not os.path.exists(output_file):
            if time.time() - start_time > timeout:
                raise ConversionEngineError("JSON was not generated")
            time.sleep(0.5)

    except Exception as e:
        raise ConversionEngineError(f"Error converting XLSX to JSON: {str(e)}")

def xlsx_to_txt(input_file: str, output_file: str): # Necesita ajuste, no se ve bien el formato
    try:
        df = pd.read_excel(input_file)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(df.to_string(index=False))

        timeout = 10
        start_time = time.time()

        while not os.path.exists(output_file):
            if time.time() - start_time > timeout:
                raise ConversionEngineError("TXT was not generated")
            time.sleep(0.5)

    except Exception as e:
        raise ConversionEngineError(f"Error converting XLSX to TXT: {str(e)}")
