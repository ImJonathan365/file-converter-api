import markdown
import os
import subprocess
import time
from app.utils.exceptions import ConversionEngineError

def md_to_pdf(input_file: str, output_file: str):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            md_text = f.read()

        html_text = markdown.markdown(md_text)

        temp_html = input_file.replace(".md", ".html")
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(html_text)

        output_dir = os.path.dirname(output_file)
        base_name = os.path.splitext(os.path.basename(temp_html))[0]
        generated_pdf = os.path.join(output_dir, base_name + ".pdf")

        command = [
            "soffice",
            "--headless",
            "--convert-to", "pdf",
            temp_html,
            "--outdir", output_dir
        ]

        subprocess.run(command, check=True)

        timeout = 10
        start_time = time.time()

        while not os.path.exists(generated_pdf):
            if time.time() - start_time > timeout:
                raise ConversionEngineError("PDF was not generated")
            time.sleep(0.5)

        os.rename(generated_pdf, output_file)

        os.remove(temp_html)

    except Exception as e:
        raise ConversionEngineError(f"Error converting MD to PDF: {str(e)}")