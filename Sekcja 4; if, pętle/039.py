n = int(input("Podaj liczbę: "))

even = []
odd = []

for n in range(1, n+1):
    if (n%2 == 0):
        even.append(n)
    else:
        odd.append(n)
print(f"Lista liczb parzystych: {even}")
print("")
print(f"Lista liczb nieparzystych: {odd}")