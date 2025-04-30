#pip install python
#pip install python-docx
#92px Arial
#dodać funkcjonalność która ogranicza dodanie zakresu ponad 100 liczb
import sys
from docx import Document
from docx.shared import Pt

def number_print_function():
    try:
        print("Podaj zakres (maksymalnie do 100)")

        start = int(input("Od: "))
        end = int(input("Do: "))
        
        numList = ' '.join(str(i) for i in range(start, end + 1))

        if (end - start > 100):
            print("Wyszedłeś poza zakres, spróbuj ponownie.")
            exit_program()

        document = Document()
        style = document.styles["Normal"]
        font = style.font
        font.name = 'Arial'
        font.size = Pt(91)
        document.add_paragraph(numList)
        document.save("Drukowanie numerków.docx")

    except ValueError as ve:
        exit_program(0)

def exit_program():
    sys.exit(0)

number_print_function()