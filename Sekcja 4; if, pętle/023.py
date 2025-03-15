# flag == True
# if flag:
# if not flag:
# PREFEROWANE ZAPISY ^

if input("Czy pada deszcz? tak / nie: ") == "nie":
    raining = False
else:
    raining = True

if input("Czy masz parasolkę? tak / nie: ") == "nie":
    haveUmbrella = False
else:
    haveUmbrella = True

temperature = float(input("Wprowadź temperaturę jaka jest na dworze: "))

if temperature >= 40 or temperature <= 0:
    print("Zostań w domu")
elif temperature > 0  and temperature < 40 and haveUmbrella and raining:
    print("Możesz wyjść z parasolką")
elif temperature >= 10 and not raining:
    print("Możesz wyjść bez parasolki")
else:
    print("Zostań w domu")