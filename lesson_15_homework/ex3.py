# Ex3 - Modulul Random
#
# RO
# Utilizand modulul random, creati un program care va simula 2 zaruri cu 6 laturi.
# Utilizatorul are optinuea sa arunce zarurile.
# Programul va afisa valorile pentru fiecare zar si valoarea totala.

import random

def throw_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("Zarul 1:", dice1)
    print("Zarul 2:", dice2)
    print("Valoarea totală:", total)

# Exemplu de utilizare
input("Apăsați ENTER pentru a arunca zarurile...")
throw_dice()
