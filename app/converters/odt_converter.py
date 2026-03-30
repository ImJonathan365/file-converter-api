import os
import subprocess
import time

def odt_to_docx(input_file: str, output_file: str):
    try:
        output_dir = os.path.dirname(output_file)
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        generated_docx = os.path.join(output_dir, base_name + ".docx")

        command = [
            "soffice",
            "--headless",
            "--convert-to", "docx",
            input_file,
            "--outdir", output_dir
        ]

        subprocess.run(command, check=True)

        timeout = 10
        start_time = time.time()

        while not os.path.exists(generated_docx):
            if time.time() - start_time > timeout:
                raise Exception("DOCX was not generated")
            time.sleep(0.5)

        os.rename(generated_docx, output_file)

    except subprocess.CalledProcessError:
        raise Exception("Error converting ODT to DOCX with LibreOffice")