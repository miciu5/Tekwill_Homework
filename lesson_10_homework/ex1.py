# Ex 1
#     De la consola se va introduce o bucata de text.
#     Calculati de cate ori fiecare cuvant a fost folosit.
#     Afisati informatia.

def numar_aparitii_cuvinte(text):
    # Transformăm textul în litere mici pentru a evita diferențierea între majuscule și minuscule
    text = text.lower()
    # Împărțim textul în cuvinte utilizând spațiul drept separator
    cuvinte = text.split()
    # Inițializăm un dicționar pentru a stoca numărul de apariții al fiecărui cuvânt
    numar_aparitii = {}

    # Iterăm prin fiecare cuvânt din lista de cuvinte
    for cuvant in cuvinte:
        # Verificăm dacă cuvântul există deja în dicționar
        if cuvant in numar_aparitii:
            # Dacă există, incrementăm numărul de apariții
            numar_aparitii[cuvant] += 1
        else:
            # Dacă nu există, adăugăm cuvântul în dicționar cu numărul de apariții inițial 1
            numar_aparitii[cuvant] = 1

    return numar_aparitii


# Introducerea textului de la consolă
text = input("Introduceți textul: ")
rezultat = numar_aparitii_cuvinte(text)

# Afisarea rezultatului
for cuvant, numar in rezultat.items():
    print(f"Cuvântul '{cuvant}' apare de {numar} ori.")