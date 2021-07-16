import pandas as pd
import tabula
import re


path = "pdf_file.pdf"

df = tabula.read_pdf(path, pages=3)

import PyPDF2
pdfFileObj = open(path, 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
print(pdfReader.numPages)

