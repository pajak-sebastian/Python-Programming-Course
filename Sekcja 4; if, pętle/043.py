nested_list = [
    [1, 2, 3],
    ["a", "b", "c"],
    [True, False, None]
]

for n_list in nested_list:
    for v in n_list:
        print(v)