"""
Time converter V2

Write a program that takes time from user input in the following format:
 "11:20 PM" or "02:00 AM".
And converts it to 24-Hour format.
"23:20" or "02:00"

Combine the solution, with the solution from the live lesson,
and make it possible that the user can decide which conversion to do.
From 24 hour to 12 hour, or vice-versa.


Convertor de timp V2

Scrie un program care preia timpul introdus de utilizator în următorul format:
"11:20 PM" sau "02:00 AM".
Și îl convertește în formatul de 24 de ore.
"23:20" sau "02:00"

Combină soluția cu soluția din lecția live
și permite utilizatorului să decidă ce conversie să facă.
De la 24 de ore la 12 ore, sau invers.
"""

# Citim timpul de la utilizator
timp = input("Introduceți timpul în formatul HH:MM AM/PM: ")

# Verificăm dacă timpul este în formatul corect
if ":" in timp and " " in timp:
    # Separăm ora, minutele și AM/PM
    ora_minut, am_pm = timp.split(" ")
    ora, minute = map(int, ora_minut.split(":"))

    # Convertem în formatul de 24 de ore
    if am_pm == "PM":
        if ora != 12:
            ora += 12
    else:
        if ora == 12:
            ora = 0

    # Construim timpul în formatul de 24 de ore
    timp_24h = f"{ora:02d}:{minute:02d}"

    # Afișăm timpul în formatul de 24 de ore
    print("Timpul în formatul de 24 de ore este:", timp_24h)
else:
    print("Formatul timpului introdus este invalid!")
