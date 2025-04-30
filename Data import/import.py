#pip install python
#pip install python-docx
#92px Cambria
from docx import Document

def number_print_function():
    print("Podaj zakres")

    start = int(input("Od: "))
    end = int(input("Do: "))
    
    numList = ' '.join(str(i) for i in range(start, end + 1))

    document = Document()
    document.add_paragraph(numList)
    document.save("Drukowanie numerków.docx")

number_print_function()