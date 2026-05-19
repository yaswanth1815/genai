import re
from docx import Document
from langchain_community.document_loaders import PyPDFLoader

def extract_text(url):

    if re.search(r"\.pdf$",url):
        text=[]
        loader=PyPDFLoader(url)
        pages=loader.load()
        for page in pages:
            line=page.page_content
            text.append(line)
        return " ".join(text)
    
    elif re.search(r"\.docx$",url):
        doc=Document(url)
        text=[]
        for line in doc.paragraphs:
            text.append(line.text)
        return " ".join(text)
    elif re.search(r"\.txt$",url):
        text=[]
        with open(url,"r") as file:
            text=file.readlines()
        return " ".join(text)