numbers = [7, 8, 9, 10, 11, 12]
print(numbers)

tupleNumbers = tuple(numbers)
print(tupleNumbers)

mixedList = ["Sebastian", 1, 1.5]
print(mixedList)

setMixed = set(mixedList)
print(setMixed, type(setMixed))

frozenSetNumbers = frozenset(tupleNumbers)
print(type(frozenSetNumbers), frozenSetNumbers)

nameAgePairs = (("Sebastian", 22), ("Seba", 21))
ageDict = dict(nameAgePairs)
print(ageDict)
print(ageDict["Sebastian"])