#
#     Creează o funcție care primește o șir de caractere ca intrare și verifică dacă este un palindrom. Gestionează eroarea de tip ValueError dacă se furnizează un șir de caractere gol.
#
# Task:
#
#     Definește o funcție care acceptă un singur parametru.
#     Verifică dacă șirul de caractere de intrare este gol folosind o instrucțiune if.
#     Dacă șirul este gol, generează o eroare de tip ValueError cu un mesaj de eroare adecvat.
#     Dacă șirul nu este gol, compară-l cu oglinditul său și returnează True dacă sunt egale (un palindrom) sau False în caz contrar.

def este_palindrom(sir):
    if len(sir) == 0:
        raise ValueError("Șirul de caractere nu poate fi gol.")
    return sir == sir[::-1]

text = "radar"
rezultat = este_palindrom(text)
print(rezultat)  # Output: True

text_gol = ""
rezultat = este_palindrom(text_gol)  # Ridică o excepție ValueError
