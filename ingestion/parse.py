def parse_pdf(path: str) -> str:
    """Parse a PDF to plain text.

    Tries `unstructured.partition.pdf.partition_pdf` first. If that's not
    available, falls back to `pymupdf` (fitz). If neither is installed, a
    RuntimeError is raised when the function is called (but importing this
    module will not fail).
    """
    try:
        from unstructured.partition.pdf import partition_pdf  # type: ignore

        elements = partition_pdf(path)
        return "\n".join([e.text for e in elements if hasattr(e, "text")])
    except Exception:
        try:
            import fitz

            doc = fitz.open(path)
            texts = []
            for page in doc:
                texts.append(page.get_text())
            return "\n".join(texts)
        except Exception:
            raise RuntimeError(
                "Missing PDF parsing dependencies. Install 'unstructured' or 'pymupdf' (pymupdf provides 'fitz')."
            )
