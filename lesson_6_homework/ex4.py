"""
Un utilizator va introduce un sir de numere, separate prin virgula de la consola.

Din sirul introdus creaza o lista de numere.

Afla suma elementelor pare si a celor impare din lista si afiseazo.
"""

# Read the input string from the user
input_string = input("Introduceți o listă de numere separate prin virgulă: ")

# Split the input string by commas to get individual numbers
numbers = input_string.split(",")

# Create a list of numbers by converting each element to integer
numbers_list = [int(num) for num in numbers]

# Initialize variables to hold the sum of even and odd numbers
sum_even = 0
sum_odd = 0

# Calculate the sum of even and odd numbers
for num in numbers_list:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

# Print the sums of even and odd numbers
print("Suma numerelor pare este:", sum_even)
print("Suma numerelor impare este:", sum_odd)
