"""
Q166. Write a function that accepts an integer and prints the
multiplication table for that number up to 10.

"""


def mul(x):
    for i in range(1, 11):
        print(f"{x} * {i} = {x*i}")


mul(2)
