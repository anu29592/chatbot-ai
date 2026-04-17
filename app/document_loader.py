from PyPDF2 import PdfReader


def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_md(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_all_documents():
    docs = []

    docs.append(load_pdf("data/contract.pdf"))
    docs.append(load_md("data/policy.md"))
    docs.append(load_txt("data/handbook.txt"))

    return docs