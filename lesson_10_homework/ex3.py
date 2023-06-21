# Ex 3
# Dat fiind două dicționare care reprezintă notele elevilor:
# math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
# science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}
# Scrieți un program care care calculeaza media notelor la fiecare elev din ambele dictionare
# si le stocheaza intr-un dictionar nou.

math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}

# Inițializare dicționar pentru stocarea mediei notelor
average_grades = {}

# Parcurgerea cheilor dintr-unul dintre dicționare (de preferat cel mai mare)
for student in math_grades.keys():
    # Verificăm dacă elevul se află în ambele dicționare
    if student in science_grades:
        # Calcularea mediei notelor pentru elev
        average = (math_grades[student] + science_grades[student]) / 2
        # Adăugarea mediei în dicționarul mediei notelor
        average_grades[student] = average

# Afișarea dicționarului cu media notelor pentru fiecare elev
print("Dicționarul cu media notelor elevilor:")
print(average_grades)