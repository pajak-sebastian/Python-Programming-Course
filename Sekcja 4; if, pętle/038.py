# Tworzenie listy kwadratów liczb
n = int(input("Wprowadź liczbę n: "))
n += 1
list = []

for v in range(1, n):
    result = v ** 2
    list.append(result)
if list:
    print(list)
else:
    print("Lista jest pusta")