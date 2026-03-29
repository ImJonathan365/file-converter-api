from app.converters.txt_converter import txt_to_pdf

CONVERTERS = {
	("txt", "pdf"): txt_to_pdf,
	# Agrega más conversiones
}

def get_converter(input_ext: str, target_ext: str):
	return CONVERTERS.get((input_ext, target_ext))
