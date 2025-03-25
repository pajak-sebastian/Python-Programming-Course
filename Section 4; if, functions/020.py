print("Pacjent może oddać krew, jeśli ma podnad 18 lat i waży więcej niż 50kg")

age = int(input("Podaj wiek pacjenta: "))
weight = int(input("Podaj wagę pacjenta: "))

if age >= 18:
    if weight >= 50:
        print("Może oddać krew")
    else:
        print("Nie może oddać krwi, za niska waga")
else:
    print("Nie może oddać krwi, za niski wiek")