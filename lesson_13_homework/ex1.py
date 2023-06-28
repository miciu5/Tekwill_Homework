#
#     Scrie o funcție care primește o listă ca intrare și returnează suma elementelor sale. Gestionează eroarea de tip TypeError dacă intrarea nu este o listă.
#
# Task:
#
#     Definește o funcție care acceptă un singur parametru.
#     Verifică dacă parametrul este de tip listă folosind o instrucțiune if.
#     Dacă parametrul este o listă, calculează suma elementelor sale folosind funcția sum() și returnează rezultatul.
#     Dacă parametrul nu este o listă, generează o eroare de tip TypeError cu un mesaj de eroare adecvat.

def calculeaza_suma(lista):
    if not isinstance(lista, list):
        raise TypeError("Parametrul trebuie să fie o listă.")
    return sum(lista)

numere = [1, 2, 3, 4, 5]
rezultat = calculeaza_suma(numere)
print(rezultat)  # Output: 15

text = "nu sunt numere"
rezultat = calculeaza_suma(text)  # Ridică o excepție TypeError
