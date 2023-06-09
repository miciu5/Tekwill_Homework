"""
Creaţi 2 liste: `elev1` şi `elev2`.

Pentru fiecare elev, cititi de la tastatură **numele**, **prenumele** şi **nota** obţinută la examen şi salvaţi datele în listele `elev1` şi `elev2`.

După aceasta, afişaţi la ecran:
* care dintre cei 2 elevi are o notă mai mare la examen (afişaţi numele şi prenumele)
* care dintre cei 2 elevi are o notă mai mică la examen (afişaţi numele şi prenumele)
* pentru fiecare elev, transformaţi numele sa fie scris cu toate literele majuscule, iar prenumele să înceapă cu literă mare. De exemplu, pentru elevul "Elon Musk", rezultatul afişat va fi "Elon MUSK"
*	afişaţi datele sub formă de tabel, folosind indexarea listelor, ca în exemplul de mai jos (Nu neaparat sa fie tabel):

| Elon | Musk | 9.5 |
|------|------|-----|
| Bill | Gates | 8.5|
"""


elev1 = []
elev2 = []

nume_elev1 = input("Introduceți numele elevului 1: ")
prenume_elev1 = input("Introduceți prenumele elevului 1: ")
nota_elev1 = float(input("Introduceți nota elevului 1: "))

elev1.append(nume_elev1)
elev1.append(prenume_elev1)
elev1.append(nota_elev1)

nume_elev2 = input("Introduceți numele elevului 2: ")
prenume_elev2 = input("Introduceți prenumele elevului 2: ")
nota_elev2 = float(input("Introduceți nota elevului 2: "))

elev2.append(nume_elev2)
elev2.append(prenume_elev2)
elev2.append(nota_elev2)

if nota_elev1 > nota_elev2:
    print(f"Elevul {nume_elev1} {prenume_elev1} are o notă mai mare la examen.")
elif nota_elev1 < nota_elev2:
    print(f"Elevul {nume_elev2} {prenume_elev2} are o notă mai mare la examen.")
else:
    print("Cei doi elevi au aceeași notă la examen.")

if nota_elev1 < nota_elev2:
    print(f"Elevul {nume_elev1} {prenume_elev1} are o notă mai mică la examen.")
elif nota_elev1 > nota_elev2:
    print(f"Elevul {nume_elev2} {prenume_elev2} are o notă mai mică la examen.")
else:
    print("Cei doi elevi au aceeași notă la examen.")

elev1[0] = elev1[0].upper()
elev1[1] = elev1[1].capitalize()
elev2[0] = elev2[0].upper()
elev2[1] = elev2[1].capitalize()

print(" {:<10} {:<10} {:<10} ".format(elev1[0], elev1[1], elev1[2]))
print(" {:<10} {:<10} {:<10} ".format(elev2[0], elev2[1], elev2[2]))
