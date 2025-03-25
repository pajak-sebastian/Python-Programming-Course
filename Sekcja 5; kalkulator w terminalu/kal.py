num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    try:
        if reset:
            num = input("Podaj pierwszą liczbę: ")
            if num == "exit":
                break
            if num == "reset":
                reset == True
                continue
            num  = int(num)
    except ValueError:
                print("Podaj liczbę!")
                continue

    operation = input(f"Podaj operację arytmetyczną: {calcOperations} ") 
    if operation == "exit":
        break
    if operation == "reset":
        reset == True
        continue

    if not operation in calcOperations:
        print("Podałeś błędną operację!")
        continue
    
    while True:
        try:
            secondNum = input("Podaj drugą liczbę: ")
            if secondNum == "exit":
                break
            if secondNum == "reset":
                reset == True
                continue
            secondNum = int(secondNum)
            break
        except ValueError:
            print("Podaj liczbę!")
            continue

    try:
        if operation == "+":
            result = num + secondNum
        elif operation == "-":
            result = num - secondNum
        elif operation == "*":
            result = num * secondNum
        elif operation == "/":
            result = num / secondNum
        elif operation == "**":
            result = num ** secondNum
    except ZeroDivisionError:
        print("Nie można dzielić przez 0 ")
        break

    print(f"Wynik: {str(num)} {operation} {str(secondNum)} = {str(result)}")

    num = result
    result = None