list_data = list(range(1, 11))

for v in list_data:
    if v > 8:               # break zatrzymuje się gdy spełni warunek
        break
    if v % 2 == 0:          # continue pomija dane iteracje, kiedy spełnią warunek
        continue
    print(f"Kwadrat: {v**2}")
else:
    print("Koniec przetwarzania")