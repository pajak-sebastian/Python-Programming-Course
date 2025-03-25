number = int(input("Podaj liczbę naturalną: "))

if number >= 0:
    i = 0
    while number > 0:
        number = number // 10
        i += 1
    if i == 0:
        i = 1
    print(i)
else:
    print("Nie podałeś liczby naturalnej")