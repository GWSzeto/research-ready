
import requests
import fitz  # PyMuPDF
from pdfminer.high_level import extract_text
from pypdf import PdfReader

# Use this as the example
#
# tree of thought paper
pdf_url = 'https://arxiv.org/pdf/2305.10601.pdf'

# The local file path where you want to save the downloaded PDF
pdf_path = 'arxiv_paper.pdf'

# Function to download the PDF
def download_pdf(url, save_path):
    response = requests.get(url)
    response.raise_for_status()  # This will raise an exception if there is a download error
    
    with open(save_path, 'wb') as f:
        f.write(response.content)
    print(f'Downloaded file saved to {save_path}')

# fitz
# Function to parse the PDF and print its text content
# def parse_pdf(file_path):
#     # Open the PDF file
#     pdf_document = fitz.open(file_path)
#     
#     # Read out the text from each page
#     for page_number in range(len(pdf_document)):
#         page = pdf_document[page_number]
#         text = page.get_text()
#         print(f'--- Page {page_number + 1} ---')
#         print(text)
#     
#     pdf_document.close()

# pdfminer six
# def parse_pdf(file_path):
#     text = extract_text(file_path)
#     print(text)

# pypdf
def parse_pdf(file_path):
    full_text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        full_text += page.extract_text()
        full_text += "\n\n"

    print(full_text)


# Main process
if __name__ == "__main__":
    # Download the PDF
    download_pdf(pdf_url, pdf_path)
    
    # Parse the downloaded PDF
    parse_pdf(pdf_path)

