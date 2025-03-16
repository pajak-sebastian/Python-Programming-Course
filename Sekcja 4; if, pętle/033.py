listData = [1, 2, 3, 4]
for v in listData:
    print(v)

tupleData = ("one", "two", "three")
for v in tupleData:
    print(v)

setData = {3, 2, 1}
for v in setData:
    print(v)

strData = "Hello"
for v in strData:
    print(v)

dictionaryData = {"Ola" : "ola@example.com", "Ania" : "ania@example.com"}
for v in dictionaryData:
    print(v)

for key, value in dictionaryData.items():
    print(f"{key} : {value}")