# Exercise 6
#
# RO
# Avand urmatorul fisier JSON: file.
# Creati un program care va afisa urmatoare informatie din fisier.
#
#     Lista de toti lucratorii
#     Lista la toate pozitiile din companie (Unicale)
#     Calculeaza suma totala care compania are de achitat lucratorii
#     Calculeaza suma totala de impozite care compania are de achitat intr-o luna
#         Valoarea de % impozit e introdusa la consola
#     Afiseaza informatie despre 10 cei mai bine platiti lucratori ((name, position, salary, employment_start_date) de la mai mult la mai putin.
#     Afiseaza informatie despre 10 lucratori cu cel mai mult timp in companie (name, position, salary, employment_start_date) de la mare la mic.

import json

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Fișierul nu a fost găsit.")
    except json.JSONDecodeError:
        print("Eroare la decodificarea fișierului JSON.")

def display_all_workers(data):
    workers = data['workers']
    print("Lista tuturor lucrătorilor:")
    for worker in workers:
        print(worker)

def display_unique_positions(data):
    positions = set()
    workers = data['workers']
    print("Lista tuturor pozițiilor unice din companie:")
    for worker in workers:
        positions.add(worker['position'])
    for position in positions:
        print(position)

def calculate_total_salary(data):
    workers = data['workers']
    total_salary = sum(worker['salary'] for worker in workers)
    print("Suma totală pe care compania o are de achitat lucrătorilor:", total_salary)

def calculate_total_taxes(data, tax_percentage):
    workers = data['workers']
    total_taxes = sum(worker['salary'] * tax_percentage / 100 for worker in workers)
    print("Suma totală de impozite pe care compania o are de achitat într-o lună (", tax_percentage, "% impozit):", total_taxes)

def display_top_10_highest_paid_workers(data):
    workers = data['workers']
    sorted_workers = sorted(workers, key=lambda x: x['salary'], reverse=True)[:10]
    print("Informații despre cei 10 cei mai bine plătiți lucrători:")
    for worker in sorted_workers:
        print(worker['name'], worker['position'], worker['salary'], worker['employment_start_date'])

def display_top_10_longest_serving_workers(data):
    workers = data['workers']
    sorted_workers = sorted(workers, key=lambda x: x['employment_start_date'], reverse=True)[:10]
    print("Informații despre cei 10 lucrători cu cel mai mult timp în companie:")
    for worker in sorted_workers:
        print(worker['name'], worker['position'], worker['salary'], worker['employment_start_date'])

# Exemplu de utilizare
file_path = 'file.json'
data = load_json_file(file_path)

if data is not None:
    display_all_workers(data)
    print()
    display_unique_positions(data)
    print()
    calculate_total_salary(data)
    print()
    tax_percentage = float(input("Introduceți procentul de impozit: "))
    calculate_total_taxes(data, tax_percentage)
    print()
    display_top_10_highest_paid_workers(data)
    print()
    display_top_10_longest_serving_workers(data)
