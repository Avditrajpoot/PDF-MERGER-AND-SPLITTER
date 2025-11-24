import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf_list, output_path):
    """
    Merge multiple PDF files into a single PDF.
    pdf_list: list of input PDF file paths
    output_path: output merged PDF path
    """
    writer = PdfWriter()

    for pdf_path in pdf_list:
        if not os.path.exists(pdf_path):
            print(f"[SKIP] File not found: {pdf_path}")
            continue

        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                writer.add_page(page)
            print(f"[OK] Added: {pdf_path}")
        except Exception as e:
            print(f"[ERROR] Could not read {pdf_path}: {e}")

    if len(writer.pages) == 0:
        print("No pages added. Merge aborted.")
        return

    with open(output_path, "wb") as out_file:
        writer.write(out_file)
    print(f"[DONE] Merged PDF saved as: {output_path}")


def split_pdf(input_pdf, output_folder):
    """
    Split one PDF into multiple single-page PDFs.
    input_pdf: path to the input PDF file
    output_folder: folder to save the split PDFs
    """
    if not os.path.exists(input_pdf):
        print(f"File not found: {input_pdf}")
        return

    os.makedirs(output_folder, exist_ok=True)

    try:
        reader = PdfReader(input_pdf)
    except Exception as e:
        print(f"[ERROR] Could not read {input_pdf}: {e}")
        return

    num_pages = len(reader.pages)
    print(f"Total pages in input PDF: {num_pages}")

    for i in range(num_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])

        output_path = os.path.join(output_folder, f"page_{i + 1}.pdf")
        with open(output_path, "wb") as out_file:
            writer.write(out_file)

        print(f"[OK] Created: {output_path}")

    print(f"[DONE] Split complete. Files saved in: {output_folder}")


def main():
    print("PDF MERGER & SPLITTER (Python)")
    print("1. Merge PDFs")
    print("2. Split a PDF")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        print("\n--- MERGE PDFs ---")
        print("Enter PDF filenames separated by commas (example: file1.pdf,file2.pdf,file3.pdf)")
        files_input = input("PDF files: ").strip()
        pdf_files = [f.strip() for f in files_input.split(",") if f.strip()]

        if not pdf_files:
            print("No valid files entered.")
            return

        output_name = input("Output merged PDF name (example: merged.pdf): ").strip()
        if not output_name.lower().endswith(".pdf"):
            output_name += ".pdf"

        merge_pdfs(pdf_files, output_name)

    elif choice == "2":
        print("\n--- SPLIT PDF ---")
        input_pdf = input("Enter input PDF filename (example: bigfile.pdf): ").strip()
        output_folder = input("Enter output folder name (example: output_pages): ").strip()

        if not output_folder:
            output_folder = "output_pages"

        split_pdf(input_pdf, output_folder)

    else:
        print("Invalid choice. Please run the program again and choose 1 or 2.")


if __name__ == "__main__":
    main()
