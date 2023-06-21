# Ex 3
# Dat fiind două dicționare care reprezintă notele elevilor:
# math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
# science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}
# Scrieți un program care care calculeaza media notelor la fiecare elev din ambele dictionare
# si le stocheaza intr-un dictionar nou.

math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}

# Inițializare dicționar pentru stocarea mediilor
averages = {}

# Parcurgerea fiecărui elev și calcularea mediei notelor
for student in math_grades:
    math_grade = math_grades.get(student, 0)
    science_grade = science_grades.get(student, 0)
    average_grade = (math_grade + science_grade) / 2
    averages[student] = average_grade

# Afișarea mediilor fiecărui elev
print("Mediile elevilor:")
for student, average in averages.items():
    print(student + ": " + str(average))