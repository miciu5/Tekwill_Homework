# Exercise 2
#
# RO:
#
# Create o programa python care deschide fiserul ex_2_file.txt gasit aici si va afisa ce contine fisierul.

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
file_path = "my_file.txt"
read_file(file_path)
