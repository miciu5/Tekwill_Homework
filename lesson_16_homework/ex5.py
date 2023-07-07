# Exercise 5
#
# RO
#
# Creati un program care va citi un fisier textual conform unui path, din input.
# Programul va afisa linia din text care are cea mai mare lungime.


def find_longest_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            longest_line = max(lines, key=lambda x: len(x))
            print("Linia cu cea mai mare lungime:")
            print(longest_line)
    except FileNotFoundError:
        print("Fișierul nu a fost găsit.")
    except OSError:
        print("A apărut o eroare la citirea fișierului.")

# Exemplu de utilizare
file_path = input("Introduceți calea fișierului: ")
find_longest_line(file_path)
