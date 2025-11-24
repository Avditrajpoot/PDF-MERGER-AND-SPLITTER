# PDF-MERGER-AND-SPLITTER
This project is a straightforward Python tool that lets users split a single PDF into several single-page PDFs or combine several PDF files into one. It offers a lightweight substitute for expensive software or manual editing by using the open-source PyPDF2 library to carry out PDF manipulation tasks programmatically.
Project Title: PDF Merger and Splitter

Project Description:
This project is a Python-based tool to merge multiple PDF files into one and to split a single PDF file into multiple single-page PDFs. It applies basic file handling and PDF manipulation techniques learned in the course using the PyPDF2 library.

Features:
- Merge multiple PDF files in a specified order into a single PDF.
- Split any PDF file into individual pages saved as separate PDF files.
- Command-line interface for user interaction.
- Error handling for file existence and reading issues.

Technologies Used:
- Python 3.x
- PyPDF2 library for PDF manipulation

Installation:
1. Install the PyPDF2 library using pip:
   pip install PyPDF2
2. Place the python script (pdf_tool.py) and your PDF files in the same directory.

Usage Instructions:
1. Run the script from a command prompt or terminal:
   python pdf_tool.py
2. Choose option 1 to merge PDFs; enter the filenames separated by commas.
3. Choose option 2 to split a PDF; provide the input filename and output directory name.
4. Output will be saved in the same directory or specified folder.

Repository Structure:
- pdf_tool.py: Main Python script with merge and split functions.
- /screenshots: Contains screenshots demonstrating tool usage and output.
- /recordings: Contains optional screen recordings of running the tool.
- README.txt: This documentation file.

Known Limitations:
- Does not support encrypted/protected PDFs.
- File paths must be correct relative to the script location.
- Limited error handling in some edge cases.

Author:
Avdit Rajpoot
25BAI11425
