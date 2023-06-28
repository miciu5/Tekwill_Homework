#
#     Creează o funcție care calculează factorialul unui număr întreg pozitiv dat. Gestionează eroarea de tip ValueError dacă este furnizat un număr care nu este întreg sau este negativ.
#
# Task:
#
#     Definește o funcție care acceptă un singur parametru.
#     Verifică dacă parametrul este un număr întreg mai mare sau egal cu zero folosind o instrucțiune if.
#     Dacă parametrul nu este un număr întreg sau este negativ, generează o eroare de tip ValueError cu un mesaj de eroare adecvat.
#     Dacă parametrul este un număr întreg pozitiv valid, calculează factorialul acestuia folosind o buclă.
#
# Returnează factorialul ca rezultat.

def factorial(numar):
    if not isinstance(numar, int) or numar < 0:
        raise ValueError("Numărul trebuie să fie un număr întreg pozitiv.")

    rezultat = 1
    for i in range(1, numar + 1):
        rezultat *= i

    return rezultat
n = 5
rezultat = factorial(n)
print(rezultat)  # Output: 120

m = -7
rezultat = factorial(m)  # Ridică o excepție ValueError
