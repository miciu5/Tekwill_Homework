"""
Nota trecătoare la un test.
Presupunem că pentru a avea o notă trecătoare la un test,
elevii trebuie să obţină minim 15 puncte.
Scrieţi un program care citeşte de la tastatură punctajul obţinut de un elev şi
afişează dacă elevul are o notă trecătoare sau va trebui să mai susţină încă o dată testul.
"""

punctaj = int(input("Introduceți punctajul obținut: "))

if punctaj >= 15:
    print("Aveți o notă trecătoare.")
else:
    print("Nu ați obținut nota trecătoare. Va trebui să mai susțineți testul.")