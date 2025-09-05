def parse_document(file_path: str) -> str:
    """
    Dummy parser: reads text from uploaded file.
    Extend later with PDF/Docx parsing logic.
    """
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
