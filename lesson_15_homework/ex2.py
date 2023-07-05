# Ex2 - Bulk Rename
#
# RO:
# Utilizand functiile dezvolatate in exercitiu 1 (de mai sus) creaza un program care va lua ca input un path la un folder.
# ATENTIE: Folositi o mapa pentru test, cu fisiere incluse acolo doar pentru test, nu folositi mape personale sa nu fie afectate fisierele.
# Programul va trebui sa redenumeasca toate fisierele in acea mapa in numere (de la 1 la n), ordonate dupa data de create a acelor fisiere. os.path.getctime(file_path) - va intoarce data de creare a fisierului.
# Programul nu trebuie sa rescrie extensia fisierului. fisier.extensie - De exemplu document.docx va trebuie sa fie re-scris ca 1.docx.
# Adaugati optiunea de a specifica un prefix: De exemplu, prefixul doc va redenumi toate fisierele in urmatorul mod doc1.docx, doc2.png, doc3.pdf, doc4.docx....

import os
import shutil

def bulk_rename_files(directory_path, prefix=""):
    if not os.path.exists(directory_path):
        print("Calea introdusă nu există.")
        return

    if not os.path.isdir(directory_path):
        print("Calea introdusă nu este un director.")
        return

    files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

    if len(files) == 0:
        print("Nu există fișiere în directorul specificat.")
        return

    files.sort(key=lambda x: os.path.getctime(os.path.join(directory_path, x)))

    for i, file in enumerate(files):
        _, file_extension = os.path.splitext(file)
        new_file_name = f"{prefix}{i+1}{file_extension}"
        new_file_path = os.path.join(directory_path, new_file_name)
        old_file_path = os.path.join(directory_path, file)
        shutil.move(old_file_path, new_file_path)
        print(f"Fișierul {file} a fost redenumit în {new_file_name}")

# Exemplu de utilizare
directory_path = input("Introduceți calea directorului: ")
prefix = input("Introduceți prefixul (lăsați gol pentru a nu adăuga niciun prefix): ")
bulk_rename_files(directory_path, prefix)
