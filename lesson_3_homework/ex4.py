"""Scrieţi un program care citeşte de la tastatură de 3 ori timpul în care un sportiv aleargă proba de 100 metri
(numărul de secunde).
Apoi afişaţi la ecran timpul mediu (media aritmetică a celor 3 încercări) în secunde."""

timp_1 = float(input("Introduceti timpul pentru incercare 1: "))
timp_2 = float(input("Introduceti timpul pentru incercare 2: "))
timp_3 = float(input("Introduceti timpul pentru incercare 3: "))
timp_mediu = (timp_1 + timp_2 + timp_3) / 3
print("Timpul mediu in secunde: ", timp_mediu)
