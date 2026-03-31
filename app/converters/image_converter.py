from PIL import Image
import os
import time
from app.utils.exceptions import ConversionEngineError

def image_to_pdf(input_file: str, output_file: str):
    try:
        image = Image.open(input_file)

        images = []

        try:
            while True:
                img = image.convert("RGB")
                images.append(img)
                image.seek(image.tell() + 1)
        except EOFError:
            pass

        if len(images) == 1:
            images[0].save(output_file, "PDF", resolution=100.0)
        else:
            images[0].save(output_file, save_all=True, append_images=images[1:])

        timeout = 10
        start_time = time.time()

        while not os.path.exists(output_file):
            if time.time() - start_time > timeout:
                raise ConversionEngineError("PDF was not generated")
            time.sleep(0.5)

    except Exception as e:
        raise ConversionEngineError(f"Error converting image to PDF: {str(e)}")