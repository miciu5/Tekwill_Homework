# Write a program that uses a while loop to check if a given positive integer n is a prime number. A prime number is a
# positive integer greater than 1 that has no positive divisors other than 1 and itself. The program should output whether
# the number is prime or not.

def is_prime_number(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            return False  # Found a divisor other than 1 and itself, not a prime number
        divisor += 1

    return True  # No divisors other than 1 and itself, prime number

# Input a positive integer
n = int(input("Enter a positive integer: "))

result = is_prime_number(n)

if result:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
