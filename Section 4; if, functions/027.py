user_input = input("Wprowadź liczby, z których ma być obliczona średnia: ").split()
num = list(map(int, user_input)) # konwersja listy na int
# print(type(num[1])) //sprawdzenie typu elementu listy
# print(num)

if len(num) > 0:
    avarage = sum(num) / len(num)
    print(f"Średnia arytmetyczna wynosi: {avarage}")
else:
    print("Nie można obliczyć średniej")