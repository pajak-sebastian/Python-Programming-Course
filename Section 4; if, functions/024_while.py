# number = int(input("Wprowadź numer do pętli: "))

# while number > 0:
#     print(number)
#     number -= 1

num = 0
while True:
    strData = input("Wprowadź liczbę, lub exit aby zakończyć: ")
    if strData == "exit":
        break
    num += int(strData)
    print(f"Wartość po dodaniu liczby: {num}")