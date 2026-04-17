from pathlib import Path
from PyPDF2 import PdfReader


def load_pdf(path: str) -> str:
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def load_txt(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def load_md(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


FILES = {
    "data/contract.pdf": load_pdf,
    "data/policy.md":    load_md,
    "data/handbook.txt": load_txt,
}


def load_all_documents() -> list[str]:
    docs = []
    for path, loader in FILES.items():
        if not Path(path).exists():
            print(f"Warning: {path} not found, skipping.")
            continue
        print(f"Loading: {path}")
        docs.append(loader(path))
    return docs