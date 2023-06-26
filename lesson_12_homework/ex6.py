# Exercițiul 6: Verificator de Palindrom
#
# Scrieți o funcție Python numită is_palindrome care verifică dacă un șir de caractere dat este un palindrom. Funcția ar trebui să primească un singur argument: text (șir de caractere) care reprezintă textul de verificat. Funcția ar trebui să returneze o valoare booleană care indică dacă textul este un palindrom.
#
# Sugestie: Un palindrom este un cuvânt, o frază, un număr sau o altă secvență de caractere care se citește la fel înainte și înapoi, fără a ține cont de spații, semne de punctuație și capitalizare.
#
# Scrieți un program care utilizează funcția is_palindrome pentru a face următoarele:
#
#     Solicitați utilizatorului să introducă un text.
#     Apelați funcția is_palindrome cu valoarea introdusă.
#     Afișați dacă textul este un palindrom sau nu.
#
# Exemplu de rezultat:
#
# Introduceți un text: radar
# Palindrom: True

def is_palindrome(text):
    # Eliminăm spațiile și convertim textul în litere mici
    text = text.replace(" ", "").lower()

    # Verificăm dacă textul este egal cu textul inversat
    return text == text[::-1]


text = input("Introduceți un text: ")

palindrom = is_palindrome(text)
print("Palindrom:", palindrom)

if palindrom:
    print("Textul este un palindrom")
else:
    print("Textul nu este un palindrom")

#
# Introduceți un text: Hello
# Palindrom: False
#
# Notă: Verificatorul de palindrom poate fi personalizat pentru a ignora sau considera spații, semne de punctuație sau capitalizare în funcție de preferințele dvs.