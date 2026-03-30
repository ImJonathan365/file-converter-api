import pandas as pd
import os
import time

def csv_to_xlsx(input_file: str, output_file: str):
    try:
        df = pd.read_csv(input_file)
        df.to_excel(output_file, index=False)

        timeout = 10
        start_time = time.time()

        while not os.path.exists(output_file):
            if time.time() - start_time > timeout:
                raise Exception("XLSX was not generated")
            time.sleep(0.5)

    except Exception as e:
        raise Exception(f"Error converting CSV to XLSX: {str(e)}")