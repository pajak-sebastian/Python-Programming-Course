def calculateHumanYears(dogYears):
    if dogYears <= 2:
        humanAge = dogYears * 10.5
    else:
        humanAge = 21 + (dogYears - 2) * 4
    return humanAge

while True:
    dogYears = float(input("Wprowadź wiek psa: "))
    if dogYears == "exit":
        break
    result = calculateHumanYears(dogYears)
    print(f"Wiek psa w ludzkich latach wynosi: {result}")