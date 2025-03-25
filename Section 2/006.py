lista = ['Zero' , 'Jeden' , 'Dwa' , 'Trzy' , 4 , 5 , 6 , 7 , 8]
lista[1] = 1        # modyfikacja elementów listy
del lista[2]        # usunięcie elementu listy
print(lista[0:4])   # wypisanie listy od 0 do 4 indeksu
print(lista[3:5])
print(lista[::2])   # wypisanie listy co 2 indeks
print(lista[::3])

if 'Trzy' in lista:
    print('Trzy jest w liście')
