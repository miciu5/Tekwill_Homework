"""Verificarea unui palindrom, Scrieți un program care primește un șir de caractere ca intrare
și verifică dacă acesta este un palindrom (se citește la fel în ambele sensuri).
"""
string=input(("Introduceti caractere: "))
if(string==string[::-1]):
      print("Este un palindrom!")
else:
      print("Nu este un palindrom")