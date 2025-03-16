number_of_elements = int(input("Podaj liczbę elementów: "))

sum = 0

if number_of_elements > 0:
    i = number_of_elements

    while i > 0:
        i -= 1

        num = float(input("Podaj liczbę: "))
        sum += num

    average = sum / number_of_elements
    print("Średnia: ", average)
else:
    print("Nie można obliczyć średniej")