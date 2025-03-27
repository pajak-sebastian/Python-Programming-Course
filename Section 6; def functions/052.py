def displayShoppingList(shoppingList):
    print("Twoja lista zakupów: ")
    for item in shoppingList:
        print(f" - {item}")

shoppingList = []

while True:
    product = input("Wpisz kolejny produkt do listy: ")
    if product == "koniec":
        break
    shoppingList.append(product)

displayShoppingList(shoppingList)