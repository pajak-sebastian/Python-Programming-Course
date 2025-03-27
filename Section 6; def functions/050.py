def findLargest(num1, num2):
    if num1 > num2:
        print(f"{num1} jest wiekszą liczbą od {num2}")
        return num1
    elif num2 > num1:
        print(f"{num2} jest większą liczbą od {num1}")
        return num2
    else:
        print(f"Są równe ({num1})")
        return num1
    
num1 = int(input("Wprowadź liczbę num1: "))
num2 = int(input("Wprowadź liczbę num2: "))

d = findLargest(num1, num2)
a = findLargest(3, 10)
b = findLargest(12, 7)
c = findLargest(1, 1)