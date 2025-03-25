num = int(input("Podaj liczbę dodatnią: "))

if num > 0:
    while num >= 0:
        print(num)
        num -= 1
    print("Odliczanie zakończone")
else:
    print("Podana liczba nie jest dodatnia")