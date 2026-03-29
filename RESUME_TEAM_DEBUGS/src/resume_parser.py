import pdfplumber
import os
from docx import Document
import io

def parse_resume(resume_file):
    """
    Parses a resume file (PDF or DOCX) and returns its text content.
    """
    filename = resume_file.filename
    _, file_extension = os.path.splitext(filename)
    
    # Read the file content into a byte stream once
    file_stream = io.BytesIO(resume_file.read())

    if file_extension.lower() == '.docx':
        document = Document(file_stream)
        text = " ".join([paragraph.text for paragraph in document.paragraphs])
    elif file_extension.lower() == '.pdf':
        with pdfplumber.open(file_stream) as pdf:
            text = " ".join([page.extract_text() for page in pdf.pages])
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX.")

   