#
#     Creează o funcție care primește o listă de numere ca intrare și calculează media geometrică a acestora. Gestionează eroarea de tip ZeroDivisionError dacă lista conține un zero.
#
# Task:
#
#     Definește o funcție care acceptă un singur parametru (o listă).
#     Verifică dacă lista conține zero folosind o instrucțiune if.
#     Dacă lista conține zero, generează o eroare ZeroDivisionError cu un mesaj de eroare adecvat.
#     Dacă lista nu conține zero, calculează produsul tuturor numerelor din listă folosind o buclă.
#     Folosește funcția math.pow() pentru a calcula media geometrică prin ridicarea produsului la puterea 1 împărțită la lungimea listei.
#     Returnează media geometrică ca rezultat.

import math

def media_geometrica(lista):
    if 0 in lista:
        raise ZeroDivisionError("Lista conține zero. Nu se poate calcula media geometrică.")

    produs = 1
    for numar in lista:
        produs *= numar

    media = math.pow(produs, 1 / len(lista))
    return media
numere = [2, 4, 8, 16]
rezultat = media_geometrica(numere)
print(rezultat)  # Output: 5.656854249492381

numere_zero = [3, 0, 6, 9]
rezultat = media_geometrica(numere_zero)  # Ridică o excepție ZeroDivisionError
