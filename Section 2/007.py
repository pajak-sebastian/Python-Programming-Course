data = [0, 1, 2, 3, 4, 5, 6]
# print(data[2])
print(len(data))
del data[2]
print(len(data))
print(data)

num = int(input("Wprowadź numer który chcesz sprawdzić w liście: "))
if num in data:
    print(f"{num} znajduje się w liście")
else:
    print(f"{num} nie znajduje się w liście")

for el in data:
    print("Elementy listy pomnożony razy 2", el * 2)