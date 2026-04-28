import fitz
import docx
from PIL import Image
import pytesseract
import os


def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    return text


def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])


def extract_text_from_image(file_path: str) -> str:
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)


def extract_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)

    elif ext == ".docx":
        return extract_text_from_docx(file_path)

    elif ext in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(file_path)

    return ""