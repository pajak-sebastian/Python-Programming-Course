dog_age = float(input("Wprowadź wiek psa w latach: "))

if dog_age <= 1:    
    human_age = dog_age * 15    #wiek "ludzki", jeśli jest równy 1
    print(f"Wiek psa wynosi: {human_age}")
elif dog_age <= 2:
    human_age = 15 + (dog_age - 1) * 9  #wiek "ludzki", jesli jest większy lub równy 2
    print(f"Wiek psa wynosi: {human_age}")
elif dog_age > 2:
    human_age = 24 + (dog_age - 2) * 5  #wiek "ludzki", jeśli jest większy od 2
    print(f"Wiek psa wynosi: {human_age}")
else:
    print("Błędna wartość")