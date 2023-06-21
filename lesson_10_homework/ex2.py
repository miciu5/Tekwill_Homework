# Ex 2
# Creaza un program care va inregistra o lista de oaspeti si comenzile lor la un restaurant.
# Utilizatorul va introduce la consola cati oaspeti vor fi inregistrati.
# Pentru fiecare oaspete, utilizatorul va introduce Numele Oaspetelui si 2 feluri de mancare.
# La sfarsit, programul va trebui sa afiseze lista cu oaspeti, ce au comandat, si cat in total va trebui restaurantul sa pregateasca.
# Fositi dict

# Inițializare dicționar gol pentru stocarea datelor comenzilor
comenzi = {}

# Citirea numărului de oaspeți de la utilizator
numar_oaspeti = int(input("Introduceți numărul de oaspeți: "))

# Înregistrarea datelor pentru fiecare oaspete
for i in range(numar_oaspeti):
    nume = input("Introduceți numele oaspetelui: ")
    fel_mancare1 = input("Introduceți primul fel de mâncare comandat: ")
    fel_mancare2 = input("Introduceți al doilea fel de mâncare comandat: ")

    # Adăugarea datelor în dicționarul comenzilor
    comenzi[nume] = [fel_mancare1, fel_mancare2]

# Afișarea listei de oaspeți
print("Lista cu oaspeți:")
for nume in comenzi.keys():
    print(nume)

# Afișarea comenzilor fiecărui oaspete
print("Comenzile oaspeților:")
for nume, feluri_mancare in comenzi.items():
    print(nume + ": " + feluri_mancare[0] + ", " + feluri_mancare[1])

# Inițializare dicționar pentru stocarea numărului de porții
numar_portii = {}

# Calcularea numărului de porții pentru fiecare fel de mâncare
for nume, feluri_mancare in comenzi.items():
    for fel in feluri_mancare:
        if fel not in numar_portii:
            numar_portii[fel] = 1
        else:
            numar_portii[fel] += 1

# Afișarea numărului de porții pentru fiecare fel de mâncare
print("Numărul de porții pentru fiecare fel de mâncare:")
for fel, numar in numar_portii.items():
    print(fel + " - " + str(numar) + " porții")