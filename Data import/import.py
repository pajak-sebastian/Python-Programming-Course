#pip install python
#pip install python-docx
#91px Arial
#dodać funkcjonalność która ogranicza dodanie zakresu ponad 100 liczb
import sys
import os
from docx import Document
from docx.shared import Pt

def number_print_function():
    try:
        print("Podaj zakres (maksymalnie do 100)")

        start = int(input("Od: "))
        end = int(input("Do: "))

        if (end - start) > 100:
            print("Wyszedłeś poza zakres, spróbuj ponownie.")
            exit_program()
        
        if end < start:
            print("Zakres musi być rosnący.")
            exit_program()

        numList = ' '.join(str(i) for i in range(start, end + 1))

        document = Document()
        desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")
        file_path = os.path.join(desktop_path, "Wydrukowane numery.docx")
        style = document.styles["Normal"]
        font = style.font
        font.name = 'Arial'
        font.size = Pt(91)
        document.add_paragraph(numList)
        document.save(file_path)

    except ValueError as ve:
        exit_program()

def exit_program():
    sys.exit(0)

number_print_function()
print("Zapis się udał.")