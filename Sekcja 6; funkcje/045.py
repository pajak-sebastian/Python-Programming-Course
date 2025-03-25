a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

def addNumbers(a,b):
    return a + b

def subNumbers(a,b):
    return a - b

def multiplyNumbers(a,b):
    return a * b

c = addNumbers(a,b)
print(f"{a} + {b} = {c}")

d = subNumbers(a,b)
print(f"{a} - {b} = {d}")

e = multiplyNumbers(a,b)
print(f"{a} * {b} = {e}")

def addAll(c, d, e):
    result = c + d + e
    return result

sumAll = addAll(c, d, e)
print(f"{c} + {d} + {e} = {sumAll}")