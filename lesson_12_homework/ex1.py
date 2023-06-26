# Introduceți temperatura: 25
# Introduceți unitatea curentă (C/F): C
# Temperatura convertită: 77.0 F
#
# Introduceți temperatura: 98.6
# Introduceți unitatea curentă (C/F): F
# # Temperatura convertită: 37.0 C

def convert_temperature(temperatura, unitate):
    if unitate == "C":
        temperatura_convertita = (temperatura * 9/5) + 32
        unitate_convertita = "F"
    elif unitate == "F":
        temperatura_convertita = (temperatura - 32) * 5/9
        unitate_convertita = "C"
    else:
        raise ValueError("Unitate invalidă. Vă rugăm utilizați 'C' pentru Celsius sau 'F' pentru Fahrenheit.")

    return temperatura_convertita, unitate_convertita


temperatura = float(input("Introduceți temperatura: "))
unitate = input("Introduceți unitatea ('C' pentru Celsius sau 'F' pentru Fahrenheit): ")

temperatura_convertita, unitate_convertita = convert_temperature(temperatura, unitate)
print(f"Temperatura convertită este: {temperatura_convertita} {unitate_convertita}")
