import os
import subprocess
import time

def txt_to_pdf(input_file: str, output_file: str):    
    try:
        output_dir = os.path.dirname(output_file)
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        generated_pdf = os.path.join(output_dir, base_name + ".pdf")

        command = [
            "soffice",
            "--headless",
            "--convert-to", "pdf",
            input_file,
            "--outdir", output_dir
        ]

        subprocess.run(command, check=True)

        timeout = 10
        start_time = time.time()

        while not os.path.exists(generated_pdf):
            if time.time() - start_time > timeout:
                raise Exception("PDF was not generated")
            time.sleep(0.5)

        os.rename(generated_pdf, output_file)

    except subprocess.CalledProcessError:
        raise Exception("Error converting TXT to PDF with LibreOffice")