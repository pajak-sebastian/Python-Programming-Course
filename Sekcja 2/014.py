a = 1 
addr1 = id(a)

a += 1
addr2 = id(a)

a += 1
addr3 = id(a)

print(addr1)
print(addr2)
print(addr3)