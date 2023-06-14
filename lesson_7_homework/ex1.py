# EN
#
# All of the following exercises should be solved using while loops without using break.
# Exercise 1: Factorial calculation
# Write a program that uses a while loop to calculate the factorial of a given positive integer n.
# The factorial of a number is the product of all positive integers from 1 to n.


def calculate_factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0:
        return 1  # Factorial of 0 is 1
    else:
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
            if n <= 1:
                n = 0  # Set n to 0 to exit the loop naturally
        return factorial

# Input a positive integer
n = int(input("Enter a positive integer: "))

result = calculate_factorial(n)

if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {n} is: {result}")
