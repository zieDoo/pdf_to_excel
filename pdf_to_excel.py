import os
import PyPDF2

folder_path = 'pdfs'


def extract_pdf_details(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    num_pages = pdf_reader.getNumPages()
    title = pdf_reader.getDocumentInfo.title

    pdf_file.close()

    return {"Number of Pages": num_pages, "Title": title}



pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

""" print(pdf_files)

print(extract_pdf_details(folder_path))

 """

print(pdf_files[0])

pdf_file = open(os.path.join(folder_path, pdf_files[0]), 'rb')

print(pdf_file)

pdf_reader = PyPDF2.PdfFileReader(pdf_file)

title2 = pdf_reader.getDocumentInfo().title
page = pdf_reader.getPage(0)

text = page.extractText()

print(text)