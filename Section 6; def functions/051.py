def cToF(celsius):
    fahrenheit = celsius * 9 / 5 +32
    return fahrenheit

def fToC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

celsius = int(input("Wprowadź stopnie Celsjusza: "))
fahrenheit = int(input("Wprowadź stopnie Fahrenheita: "))

ctof = cToF(celsius)
print(f"20 stopni Celsjusza to {ctof} stopni Fahrenheita")

ftoc = fToC(fahrenheit)
print(f"86 stopni Fahrenheita to {ftoc} stopni Celsjusza")