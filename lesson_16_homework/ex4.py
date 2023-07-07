# Exercise 4
#
# RO:
#
# Creati un program care va avea 2 optiuni:
#     Afiseaza toate bucatele
#         Va afisa toate bucatele stocate intr-un fisier
#     Adauga bucata
#         Va adauga o bucata in lista din fisier
#
# Daca utilizatorul re-porneste programul, la afisarea bucatelor, trebuie sa fie afisate toate elementele salvate anterior.

def display_dishes(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Lista cu bucate:")
            print(content)
    except FileNotFoundError:
        print("Fișierul nu a fost găsit.")
    except OSError:
        print("A apărut o eroare la citirea fișierului.")

def add_dish(file_path, dish):
    try:
        with open(file_path, 'a') as file:
            file.write(dish)
            file.write("\n")
            print("Bucata a fost adăugată în listă.")
    except OSError:
        print("A apărut o eroare la scrierea în fișier.")

# Exemplu de utilizare
file_path = "lista_bucate.txt"

while True:
    print("Opțiuni:")
    print("1. Afisează toate bucatele")
    print("2. Adaugă bucata")
    print("3. Ieși din program")
    choice = input("Introduceți opțiunea dorită: ")

    if choice == "1":
        display_dishes(file_path)
    elif choice == "2":
        dish = input("Introduceți bucata: ")
        add_dish(file_path, dish)
    elif choice == "3":
        break
    else:
        print("Opțiune invalidă. Încercați din nou.")

