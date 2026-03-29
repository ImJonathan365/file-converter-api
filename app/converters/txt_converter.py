def txt_to_pdf(input_path: str, output_path: str):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    y = height - 40

    for line in lines:
        c.drawString(40, y, line.strip())
        y -= 15

        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
