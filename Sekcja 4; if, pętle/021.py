experience = int(input("Wpisz staż pracy kandydata: "))
languages = input("Wpisz, oddzielając spacją, języki z którymi kandydat ma doświadczenie: ").split() #["python", "typescript", "javascript", "java"]
contractType = input("Wpisz typ kontraktu, który chce kandydat: ")

if experience >= 2 and "python" and "java" in languages:
    if contractType == "b2b" or contractType == "employment":
        print("Kandydat został przyjęty")
    else:
        print("Kandydat nie spełnia wymagań typu zatrudnienia.")
else:
    print("Kandydat nie spełnia warunków")