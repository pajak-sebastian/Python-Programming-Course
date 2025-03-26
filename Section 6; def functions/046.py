def sumListElements(listData):
    if len(listData) == 0:
        print("Lista jest pusta!")
        return None
    result = 0
    for v in listData:
        result += v
    return result

print(sumListElements([]))
print(sumListElements([1,2,3,4,5]))

def printList(listData):
    if len(listData) == 0:
        return
    for v in listData:
        print(v)

printList([])
printList([1,2,3,5])