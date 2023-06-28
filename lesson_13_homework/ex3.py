#
#     Scrie un program care cere utilizatorului să introducă două numere și calculează împărțirea lor. Gestionează eroarea de tip ZeroDivisionError dacă al doilea număr este zero.
#
# Task:
#
#     Cere utilizatorului să introducă primul număr și stochează-l într-o variabilă.
#     Cere utilizatorului să introducă al doilea număr și stochează-l într-o altă variabilă.
#     Convertiți ambele intrări în numere cu zecimale folosind funcția float().
#     Împarte primul număr la al doilea număr și stochează rezultatul într-o variabilă.
#     Folosește un bloc try-except pentru a gestiona eroarea ZeroDivisionError și afișează un mesaj de eroare adecvat dacă al doilea număr este zero.
#     Dacă împărțirea este reușită, afișează rezultatul.

try:
    numar1 = float(input("Introdu primul număr: "))
    numar2 = float(input("Introdu al doilea număr: "))

    rezultat = numar1 / numar2
    print("Rezultatul împărțirii este:", rezultat)

except ZeroDivisionError:
    print("Eroare: Al doilea număr este zero. Nu se poate realiza împărțirea.")
