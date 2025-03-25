import random

rand_num = random.randint(1, 10)
print(rand_num)
user_num = int(input("Zgadnij liczbę od 1 do 10: "))

if user_num >= 1 and user_num <= 10:
        if rand_num == user_num:
            print("Poprawny numer")
        else:
            print("Żle, spróbuj ponownie")

else:
    print("Podałeś numer niepasujący do zakresu")