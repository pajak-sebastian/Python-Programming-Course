print("Kalkulator BMI")

waga = input("Podaj wagę w kg: ")
wzrost = input("Podaj wzrost w m: ")

waga = int(waga)
wzrost = float(wzrost)

bmi = waga / (wzrost*wzrost)
bmi = round(bmi, 2)
 
print(f"Twoje bmi wynosi {bmi}")