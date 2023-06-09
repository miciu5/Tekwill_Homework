"""
Creaţi lista `date_personale`.

Citiţi după aceasta de la tastatură **numele**, **prenumele**, **vârsta**, **înălţimea** şi **ocupaţia** utilizatorului şi adăugaţi aceste valori în lista creată.
"""
date_personale = []

nume = input("Introduceți numele: ")
prenume = input("Introduceți prenumele: ")
varsta = input("Introduceți vârsta: ")
inaltimea = input("Introduceți înălțimea: ")
ocupatia = input("Introduceți ocupația: ")

date_personale.append(nume)
date_personale.append(prenume)
date_personale.append(varsta)
date_personale.append(inaltimea)
date_personale.append(ocupatia)

print(date_personale)