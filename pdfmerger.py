import os
from PyPDF2 import PdfReader , PdfWriter, PdfMerger

def merge_pdfs(input_dir, output_filename):
    pdf_merger = PdfMerger()
    
    # Get all the files in the folder and sort them in alphabetical order.
    files = sorted(os.listdir(input_dir))
    
    # Process only the PDF files.
    pdf_files = [file for file in files if file.endswith('.pdf')]
    
    # Merge the PDF files.
    for file in pdf_files:
        file_path = os.path.join(input_dir, file)
        pdf_merger.append(file_path)
    
    # Create the merged PDF.
    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

input_directory = input("PDF Dosya Yolu: ")
output_file = 'merged_file.pdf'

merge_pdfs(input_directory, output_file)