# File Converter API

A file conversion REST API built with FastAPI.
This API allows users to upload files such as Word documents, Excel spreadsheets, PDFs, images, and text files, and convert them into different formats like PDF, DOCX, CSV, JSON, TXT, HTML, and Markdown.

---

## Features

* Upload and convert files
* Supports multiple file formats
* FastAPI REST API
* Multiple conversion engines depending on file type
* Clean architecture
* Docker support
* Scalable architecture
* Ready for cloud deployment

---

## Supported Conversions

| From | To   |
| ---- | ---- |
| DOCX | PDF  |
| DOCX | TXT  |
| DOCX | HTML |
| DOCX | MD   |
| ODT  | DOCX |
| TXT  | PDF  |
| MD   | PDF  |
| XLSX | CSV  |
| XLSX | JSON |
| XLSX | TXT  |
| CSV  | XLSX |
| PDF  | DOCX |
| JPG  | PDF  |
| JPEG | PDF  |
| PNG  | PDF  |
| BMP  | PDF  |
| TIFF | PDF  |

---

## Tech Stack

* FastAPI
* Pandoc (via pypandoc)
* Pandas
* pdf2docx
* Pillow
* img2pdf
* Python
* Docker
* Uvicorn

---

## Installation


---

## License

MIT License

---

## Author

Software Developer | Business Informatics
