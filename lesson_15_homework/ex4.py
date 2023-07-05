# Ex 4 - Improve Ex 3
#
# RO
# Imbunatatiti exercitiul de mai sus pentru a permite utilizatorului sa aleaga cate laturi va avea zarul si cate zaruri sa arunce.
# Dupa ce zarurile au fost configurate, permiteti utilizatorului sa arunce de un numar indefinit de ori (pan la STOP).

import random

def throw_dice(num_dice, num_faces):
    for _ in range(num_dice):
        dice_value = random.randint(1, num_faces)
        print("Valoarea zarului:", dice_value)

# Exemplu de utilizare
num_dice = int(input("Introduceți numărul de zaruri: "))
num_faces = int(input("Introduceți numărul de fețe al zarului: "))

while True:
    user_input = input("Apăsați ENTER pentru a arunca zarurile (sau introduceți 'STOP' pentru a opri): ")
    if user_input == "STOP":
        break
    throw_dice(num_dice, num_faces)
