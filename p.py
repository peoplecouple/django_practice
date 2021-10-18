import pdfplumber

def plum_daldal(filename):
    with pdfplumber.open(filename) as pdf:
        page = pdf.pages[0]
        print(pdf.pages)
        print(page.extract_text())

plum_daldal("아뱅.pdf")