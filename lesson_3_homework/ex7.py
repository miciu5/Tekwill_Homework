"""Numărarea caracterelor
Scrieți un program care primește un șir de caractere ca intrare
și numără de câte ori apare un caracter specific (introdus in consola).
Numarul de caractere trebuie sa fie considerat indiferent daca e majuscula sau minuscula
"""

def numara_caractere(șir, caracter):
    șir_mic = șir.lower()
    numar = șir_mic.count(caracter.lower())
    return numar

șir = input("Introduceți un șir de caractere: ")
caracter = input("Introduceți caracterul pentru care doriți să numărați: ")

rezultat = numara_caractere(șir, caracter)
print(f"Caracterul '{caracter}' apare de {rezultat} ori în șirul '{șir}'.")