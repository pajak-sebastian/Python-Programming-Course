try:
    num = int(input("Wprowadź dowolną liczbę: "))

    if num > 0:
        print(f"Liczba {num} jest dodatnia")
        
    elif num < 0:
        print(f"Liczba {num} jest ujemna")

    else:
        print(f" Liczba {num} wynosi zero")

except ValueError:
    print(f"To nie jest liczba")