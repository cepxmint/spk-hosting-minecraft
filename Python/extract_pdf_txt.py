import pdfplumber
from pathlib import Path

materi_dir = Path(__file__).parent.parent / "Materi"

pdf_files = sorted(materi_dir.glob("*.pdf"))

for pdf_path in pdf_files:
    print(f"Extracting: {pdf_path.name} ...")

    text_pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pdf.pages if hasattr(pdf, 'pdf') else pdf.pages, 1):
            text = page.extract_text()
            if text:
                text_pages.append(f"--- Halaman {i} ---\n{text}")

    txt_path = pdf_path.with_suffix(".txt")
    txt_path.write_text("\n\n".join(text_pages), encoding="utf-8")

    print(f"  -> {txt_path.name} ({len(text_pages)} halaman)")

print("\nSelesai! Semua PDF udah jadi TXT~")
