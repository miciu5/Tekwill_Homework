"""Cititi de la utilizator, o lista de nume, separate prin virgula.

Folosind metoda `.split()` transformati textul de la utilizator intr-o lista de nume.

Pentru fiecare nume cititi nota introdusa de utilizator (numar intreg). Adaugati nota in lista `list_of_marks`.

Apoi:
* afișați pentru fiecare nume, nota care îi aparține.
* calculați suma notelor
* calculați media notelor


Completati campurile din ___ si adaugati codul necesar.

Note: Utilizati indiciele numelui pentru a afla nota dupa indice din `list_of_marks`.
"""

names = input("Introduceți o listă de nume, separate prin virgulă: ")
list_of_names = names.split(",")

list_of_marks = []

for name in list_of_names:
    mark = int(input(f"Introduceți nota pentru {name}: "))
    list_of_marks.append(mark)

for i in range(len(list_of_names)):
    print(f"Nota pentru {list_of_names[i]} este {list_of_marks[i]}")

marks_sum = sum(list_of_marks)
marks_average = marks_sum / len(list_of_marks)

print(f"Suma notelor: {marks_sum}")
print(f"Media notelor: {marks_average}")










