from app.converters.txt_converter import txt_to_pdf
from app.converters.docx_converter import docx_to_pdf, docx_to_txt, docx_to_html, docx_to_md
from app.converters.pdf_converter import pdf_to_docx
from app.converters.odt_converter import odt_to_docx
from app.converters.md_converter import md_to_pdf
from app.converters.xlsx_converter import xlsx_to_csv, xlsx_to_json, xlsx_to_txt
from app.converters.csv_converter import csv_to_xlsx
from app.converters.image_converter import image_to_pdf

CONVERTERS = {
	("txt", "pdf"): txt_to_pdf,
	("docx", "pdf"): docx_to_pdf,
	("docx", "txt"): docx_to_txt,
	("docx", "html"): docx_to_html,
	("docx", "md"): docx_to_md,
	("pdf", "docx"): pdf_to_docx,
	("odt", "docx"): odt_to_docx,
	("md", "pdf"): md_to_pdf,
	("xlsx", "csv"): xlsx_to_csv,
	("xlsx", "json"): xlsx_to_json,
	("xlsx", "txt"): xlsx_to_txt,
	("csv", "xlsx"): csv_to_xlsx,
	("jpg", "pdf"): image_to_pdf,
	("jpeg", "pdf"): image_to_pdf,
	("png", "pdf"): image_to_pdf,
	("bmp", "pdf"): image_to_pdf,
	("tiff", "pdf"): image_to_pdf,
}

def get_converter(input_ext: str, target_ext: str):
	return CONVERTERS.get((input_ext, target_ext))
