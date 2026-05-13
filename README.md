# File Converter API

A file conversion REST API built with FastAPI.
This API allows users to upload files such as Word documents, Excel spreadsheets, PDFs, images, and text files, and convert them into different formats like PDF, DOCX, CSV, JSON, TXT, HTML, and Markdown.

---

## Features

* Upload and convert files
* Multiple supported file formats
* FastAPI REST API
* LibreOffice-based document conversions
* Multiple conversion engines depending on file type
* File validation system
* MIME type validation
* File size validation
* Clean architecture
* Docker support
* Containerized LibreOffice support
* Scalable architecture

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

### Backend

* Python 3.11
* FastAPI
* Uvicorn

### Conversion Engines

* LibreOffice
* Pandoc (via pypandoc)
* pdf2docx
* Pandas
* Pillow
* img2pdf
* python-docx
* openpyxl

### Infrastructure

* Docker
* Docker Compose

---

## Project Structure

```bash
app/
├── api/
├── config/
├── converters/
├── services/
├── utils/
└── main.py
```

---

## Installation

### Local Installation

#### 1. Clone repository

```bash
git clone https://github.com/ImJonathan365/file-converter-api.git
cd file-converter-api
```

#### 2. Create virtual environment

```bash
python -m venv venv
```

#### 3. Activate virtual environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

#### 4. Install dependencies

```bash
pip install -r requirements.txt
```

#### 5. Install LibreOffice

Linux (Debian/Ubuntu):

```bash
sudo apt-get install libreoffice
```

Windows:

Download and install LibreOffice from:
https://www.libreoffice.org/download/download-libreoffice/

#### 6. Run the API

```bash
uvicorn app.main:app --reload --port 8000
```

---

## Docker Installation

### Build containers

```bash
docker compose build
```

### Run containers

```bash
docker compose up -d
```

### Stop containers

```bash
docker compose down
```

The API will be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/api/docs
```

---

## API Endpoints

| Method | Endpoint                  | Description               |
| ------ | ------------------------- | ------------------------- |
| POST   | /api/convert/             | Convert files             |
| GET    | /api/download/{filename}  | Download converted file   |
| GET    | /api/formats/             | List supported conversions|
| GET    | /api/health/              | Health check              |

---

## Example Request

### Convert DOCX to PDF

Using Postman:

- Method: `POST`
- URL:

```text
http://localhost:8000/api/convert/
```

Body → form-data:

| Key           | Type | Value          |
| ------------- | ---- | -------------- |
| file          | File | document.docx  |
| target_format | Text | pdf            |

---

## License

MIT License

---

## Author

Software Developer | Business Informatics
