# Exercițiul 3: Verificator de Putere a Parolei
#
# Scrieți o funcție
#
# Python numită check_password_strength care verifică puterea unei parole date. Funcția ar trebui să primească un singur argument: password (șir de caractere) care reprezintă parola de verificat. Funcția ar trebui să returneze o valoare booleană care indică dacă parola respectă criteriile de putere specificate.
#
# Criteriile de putere ale parolei sunt următoarele:
#
#     Cel puțin 8 caractere lungime
#     Conține cel puțin o literă majusculă
#     Conține cel puțin o literă minusculă
#     Conține cel puțin o cifră
#     Conține cel puțin un caracter special (de exemplu, !@#$%^&*)
#
# Scrieți un program care utilizează funcția check_password_strength pentru a face următoarele:
#
#     Solicitați utilizatorului să introducă o parolă.
#     Apelați funcția check_password_strength cu valoarea introdusă.
#     Afișați dacă parola respectă criteriile de putere sau nu.
#
# Exemplu de rezultat:
#
# Introduceți o parolă: MyPass123
# Puterea parolei: True (respectă criteriile)
#
# Introduceți o parolă: abcdefg
# Puterea parolei: False (nu respectă criteriile)
#
# Notă: Puteți îmbunătăți verificatorul de putere a parolei prin adăugarea de criterii suplimentare
# sau personalizarea cerințelor în funcție de preferințele dvs.

def check_password_strength(password):
    if len(password) < 8:
        return False

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in '!@#$%^&*' for char in password)

    return has_uppercase and has_lowercase and has_digit and has_special_char


parola = input("Introduceți o parolă: ")

putere_parola = check_password_strength(parola)
print("Puterea parolei:", putere_parola)

if putere_parola:
    print("Parola respectă criteriile")
else:
    print("Parola nu respectă criteriile")
