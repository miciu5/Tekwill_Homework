# Preluarea numerelor de la utilizator
numar1 = float(input("Introduceti primul numar: "))
numar2 = float(input("Introduceti al doilea numar: "))

# Adunare
suma = numar1 + numar2
print("Suma celor doua numere:", suma)

# Scadere
diferenta = numar1 - numar2
print("Diferenta dintre primul numar si al doilea numar:", diferenta)

# Inmultire
produs = numar1 * numar2
print("Produsul celor doua numere:", produs)

# Impartire
if numar2 != 0:
    impartire = numar1 / numar2
    print("Impartirea primului numar la al doilea numar:", impartire)
else:
    print("Impartirea la zero nu este definita.")

