"""
Scrieţi un program care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""

string = input("Introduceți un șir de caractere: ")

if len(string) >= 2 and string[1] == "a":
    print("Litera 'a' se află pe a 2-a poziție.")
else:
    print("Litera 'a' nu se află pe a 2-a poziție.")