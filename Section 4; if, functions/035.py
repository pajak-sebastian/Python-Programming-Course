list = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

for v in list:
    if v == 0:
        print("Zero jest parzyste")
    elif (v % 2 != 0):
        print(f"Liczba {v} jest nieparzysta")
    else:
        print(f"Liczba {v} jest parzysta")