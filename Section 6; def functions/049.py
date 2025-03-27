def calculateArea(length, width):
    rectangle = length * width
    return rectangle

a = float(input("Wprowadź długość prostokąta: "))
b = float(input("Wprowadź szerokość prostokąta: "))

result = calculateArea(a, b)
print(result)