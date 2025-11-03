"""
Q118. Write a program to find and print all prime numbers within a given
list.
"""

num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in num_list:
    if i > 1:  # prime numbers are greater than 1
        for j in range(2, i):  # check all numbers from 2 to i-1
            if i % j == 0:  # if divisible, then not a prime
                break
        else:
            print(i)

# other method

my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in my_list:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors = factors + 1
    if factors == 2:
        print(num)
