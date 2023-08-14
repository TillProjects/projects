#!/usr/bin/env python3
from PyPDF2 import PdfMerger
import re
from sys import argv


# Kombiniert pdf Dateien, welche über die Shell eingegeben werden.
# Dabei sind die ersten i pdfs die zu kombinierenden und der letzte Name,
# der von der neuen, kombinierten pdf Datei

# merge_pdfs(['file1.pdf', 'file2.pdf', 'file3.pdf'], 'output.pdf')
def merge_pdfs(pdf_list, output):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output)
    merger.close()


# Hole die Anzahl der übergebenen Dateien
n_files = len(argv) - 2

# Hole die Namen der Dateien aus den Argumenten
file_names_temp = argv[1:n_files + 1]

# Bereite die Dateinamen vor
file_names = []
for file in file_names_temp:
    # Extrahiere den Dateinamen ohne .pdf
    file_name = re.search(r'(\w+)(.pdf)?', file).group(1)
    file_names.append(f"{file_name}.pdf")

# Bereite den Namen der Ausgabedatei vor
output_name = re.search(r'(\w+)(.pdf)?', argv[n_files + 1]).group(1)
output_name = f"{output_name}.pdf"

# Kombiniere die PDFs in eine einzige Datei
merge_pdfs(file_names, output_name)

# Drucke eine Erfolgsmeldung
print('files merged')
