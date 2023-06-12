"""
BMI Calculator
Write a program that takes a person's weight (in kilograms) and height (in meters) as input and calculates
their Body Mass Index (BMI). Then classify the BMI into the following categories:

Underweight (BMI < 18.5)
Normal weight (BMI between 18.5 and 24.9)
Overweight (BMI between 25 and 29.9)
Obesity (BMI 30 or greater)


Calculator BMI
Scrie un program care primește greutatea unei persoane (în kilograme) și înălțimea (în metri) ca intrare
și calculează Indicele de Masă Corporală (BMI). Apoi clasifică BMI-ul în următoarele categorii:

Subponderal (BMI < 18,5)
Greutate normală (BMI între 18,5 și 24,9)
Supraponderal (BMI între 25 și 29,9)
Obezitate (BMI 30 sau mai mare)

Pentru a calcula Indicele de Masă Corporală (BMI), urmează pașii de mai jos:

1. Ia greutatea persoanei în kilograme și înălțimea în metri.
2. Calculează pătratul înălțimii (înmulțește înălțimea cu ea însăși).
3. Calculează BMI-ul utilizând formula: BMI = greutate / înălțime^2, unde greutatea este în kilograme și înălțimea este în metri.
4. Rezultatul obținut va fi indicele de masă corporală al persoanei.

"""

weight = float(input("Introduceți greutatea în kilograme: "))
height = float(input("Introduceți înălțimea în metri: "))

bmi = weight / (height ** 2)

print("Indicele de Masă Corporală (BMI) este:", round(bmi, 2))

if bmi < 18.5:
    print("Subponderal")
elif bmi < 24.9:
    print("Greutate normală")
elif bmi < 29.9:
    print("Supraponderal")
else:
    print("Obezitate")