"""1.	Creați 2 variabile x şi y, a căror valoare este citită de la tastatură.
Folosiți funcţia int() pentru a transforma valorile citite în numere întregi.
* Definiţi după aceasta variabila suma care va fi egală cu suma lui x şi y.
* Definiţi variabila **diff** care va fi egală cu x - y (diferenţa lui x şi y).
* Definiţi variabila **rest_impart** care va fi egală cu restul împărţirii lui x la y.
* Definiţi variabila **mult** care va fi egală cu x înmulţit cu y.
* Definiţi variabila **power3** care va fi egală cu x la puterea 3.
Afișați toate rezultatele"""

x = int(input("Introduceti valoarea x: "))
y = int(input("Introduceti valoarea y: "))
suma = x+y
dif = x-y
rest_impart = x/y
mult = x*y
power3 =x**3


print ("Suma x si y este: ", suma)
print ("Diferenta dintre x si y este: ", dif)
print ("Restul impartirii lui x la y este: ", rest_impart)
print ("Produsul lui x si y este: ", mult)
print ("x la puterea 3 este: ", power3)



