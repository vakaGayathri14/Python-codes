"""
5. write a python function that takes start_number and end_number as a parameter. Now print all the prime numbers betweeen stat_number to end_number.

"""

def primeNumbers(start_num, end_num):
    for i in range(start_num, end_num + 1):   # Loop through all numbers in range
        if i > 1:                             # Prime numbers are greater than 1
            factors = 0                       # Reset for each number
            for j in range(1, i + 1):         # Check divisors of i
                if i % j == 0:                # j divides i evenly
                    factors = factors + 1
            if factors == 2:                  # If only 2 factors (1 and itself)
                print(i, end=" ")             # Print the prime number
primeNumbers(3, 13)
