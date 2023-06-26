# Exercițiul 2: Secvența Fibonacci
#
# Scrieți o funcție Python numită generate_fibonacci care generează secvența Fibonacci până la un număr dat de termeni. Funcția ar trebui să primească un singur argument: terms (integer) care indică numărul de termeni Fibonacci de generat. Funcția ar trebui să returneze o listă care conține secvența Fibonacci.
#
# Sugestie: Secvența Fibonacci începe cu 0 și 1, iar fiecare număr ulterior este suma celor două numere precedente.
#
# Scrieți un program care utilizează funcția generate_fibonacci pentru a face următoarele:
#
#     Solicitați utilizatorului să introducă numărul de termeni Fibonacci de generat.
#     Apelați funcția generate_fibonacci cu valoarea introdusă.
#     Afișați secvența Fibonacci generată.
#
# Exemplu de rezultat:
#
# Introduceți numărul de termeni Fibonacci de generat: 8
# Secvența Fibonacci generată: [0, 1, 1, 2, 3, 5, 8, 13]
#
# Introduceți numărul de termeni Fibonacci de generat: 5
# Secvența Fibonacci generată: [0, 1, 1, 2, 3]

def generate_fibonacci(terms):
    fibonacci_sequence = [0, 1]  # Secvența Fibonacci începe cu 0 și 1

    if terms <= 2:
        return fibonacci_sequence[:terms]  # Returnează primele terms numere Fibonacci

    while len(fibonacci_sequence) < terms:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


numar_termeni = int(input("Introduceți numărul de termeni Fibonacci de generat: "))

secventa_fibonacci = generate_fibonacci(numar_termeni)
print("Secvența Fibonacci generată:", secventa_fibonacci)

