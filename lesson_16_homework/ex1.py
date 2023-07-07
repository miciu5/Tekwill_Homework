# Exercise 1
#
# RO:
#
# Create o programa python care va crea un fisier conform unui nume (sau path) introdus de la consola.

def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            print(f"Fișierul {file_path} a fost creat cu succes.")
    except OSError:
        print("A apărut o eroare la crearea fișierului.")

# Exemplu de utilizare
file_path = input("Introduceți numele sau calea fișierului: ")
create_file(file_path)
