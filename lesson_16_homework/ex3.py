# Exercise 3
#
# RO:
#
# Creati un program python care va citi numele unui fisier de la consola.
# Programul va crea un fisierl cu numele fisierului citit de la consola, apoi va intreba utilizatorul sa scrie un text.
# Textul introdus de utilizator trebuie adaugat in fisier.
# Apoi cititi din fisier textul introdus de utilizator.

def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            print(f"Fișierul {file_path} a fost creat cu succes.")
    except OSError:
        print("A apărut o eroare la crearea fișierului.")

def write_to_file(file_path, text):
    try:
        with open(file_path, 'a') as file:
            file.write(text)
            file.write("\n")
            print("Textul a fost adăugat în fișier.")
    except OSError:
        print("A apărut o eroare la scrierea în fișier.")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Conținutul fișierului:")
            print(content)
    except FileNotFoundError:
        print("Fișierul nu a fost găsit.")
    except OSError:
        print("A apărut o eroare la citirea fișierului.")

# Exemplu de utilizare
file_path = input("Introduceți numele fișierului: ")
create_file(file_path)

text = input("Introduceți textul: ")
write_to_file(file_path, text)

read_file(file_path)
