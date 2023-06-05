"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere
Note: Indiferent daca e majuscula sau minusucula litera
"""


sir_caractere = input("Introduceți un șir de caractere: ")

# Calcularea numărului total de litere
numar_litere = len([caracter for caracter in sir_caractere if caracter.isalpha()])

# Calcularea numărului de vocale
numar_vocale = len([caracter for caracter in sir_caractere.lower() if caracter in 'aeiou'])

# Calcularea numărului de consoane
numar_consoane = numar_litere - numar_vocale

print("Numărul total de litere în șirul de caractere este:", numar_litere)
print("Numărul de vocale în șirul de caractere este:", numar_vocale)
print("Numărul de consoane în șirul de caractere este:", numar_consoane)

