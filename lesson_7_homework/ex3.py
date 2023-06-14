# Exercise 3: Fibonacci sequence
# Write a program that uses a while loop to generate the Fibonacci sequence up to a given number of terms. The Fibonacci
# sequence is a series of numbers where each number is the sum of the two preceding ones. The sequence starts with 0 and


def generate_fibonacci_sequence(num_terms):
    sequence = []

    # First two terms of the sequence
    term1, term2 = 0, 1
    sequence.append(term1)
    sequence.append(term2)

    count = 2

    while count < num_terms:
        next_term = term1 + term2
        sequence.append(next_term)

        term1 = term2
        term2 = next_term

        count += 1

    return sequence

# Input the number of terms for the Fibonacci sequence
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Generate the Fibonacci sequence
fibonacci_sequence = generate_fibonacci_sequence(num_terms)

# Print the Fibonacci sequence
print(f"The Fibonacci sequence up to {num_terms} terms is:")
print(fibonacci_sequence)
