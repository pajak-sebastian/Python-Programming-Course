numbers = [-3, -2, -1, 0, 1, 2, 3]
set = {-1}

for v in numbers:
    if (v % 2 != 0):
        set.add(v)

for n in set:
    print(n)