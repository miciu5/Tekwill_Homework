""" Extrageți un subșir de caractere
Scrieți un program care primește un șir de caractere ca intrare și extrage un subșir specific din acesta,
 bazat pe pozițiile de început și sfârșit definite de utilizator."""

sir_caractere = input("Introduceți un șir de caractere: ")
inceput = int(input("Introduceți poziția de început a subșirului: "))
sfarsit = int(input("Introduceți poziția de sfârșit a subșirului: "))

subsir = sir_caractere[inceput:sfarsit]

print("Subșirul extra<|endoftext|>")