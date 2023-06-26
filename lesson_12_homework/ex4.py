# Exercițiul 4: Verificator de Număr Prim
#
# Scrieți o funcție Python numită is_prime care verifică dacă un număr dat este prim sau nu. Funcția ar trebui să primească un singur argument: number (integer) care reprezintă numărul de verificat. Funcția ar trebui să returneze o valoare booleană care indică dacă numărul este prim.
#
# Sugestie: Un număr prim este un număr mai mare decât 1 și care nu are divizori în afară de 1 și el însuși.
#
# Scrieți un program care utilizează funcția is_prime pentru a face următoarele:
#
#     Solicitați utilizatorului să introducă un număr.
#     Apelați funcția is_prime cu valoarea introdusă.
#     Afișați dacă numărul este prim sau nu.
#
# Exemplu de rezultat:
#
# Introduceți un număr: 17
# Număr prim: True
#
# Introduceți un număr: 8
# Număr prim: False

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


numar = int(input("Introduceți un număr: "))

numar_prim = is_prime(numar)
print("Număr prim:", numar_prim)

if numar_prim:
    print("Numărul este prim")
else:
    print("Numărul nu este prim")
