# Homework
# Ex 1
#
# Creati un program care va primi ca input o cale (path) de fisiere din calculator: ex: C:\Program Files\.
# Programul va trebui sa afiseze o lista de toate fisierele din mapa introdusa in input (doar fisierele, si nu alte mape).
# Daca calea introdusa nu este o mapa, programul trebuie sa arate urmatoarea eroare: Calea introdusa nu este o mapa.
# Daca calea introdusa nu exista, programul va trebuie sa arate urmatoare eroare: Calea introdusa nu exista.
# Hints:
# Use: os.path.isdir, os.path.join(), os.listdir

import os

def list_files_in_directory(directory_path):
    if not os.path.exists(directory_path):
        print("Calea introdusă nu există.")
        return

    if not os.path.isdir(directory_path):
        print("Calea introdusă nu este un director.")
        return

    files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

    if len(files) == 0:
        print("Nu există fișiere în directorul specificat.")
    else:
        print("Fișierele din directorul", directory_path, "sunt:")
        for file in files:
            print(file)

# Exemplu de utilizare
directory_path = input("Introduceți calea directorului: ")
list_files_in_directory(directory_path)
