"""
Q169. Write a function that takes an integer and prints whether it is a
prime number.

"""


def primeNumber(x=0):
    count = 0
    if x > 0:
        for i in range(2, x):
            if x % i == 0:
                count = count + 1
        if count > 0:
            print(f"{x} is Not a Prime Number")
        else:
            print(f"{x} is a Prime Number")
    else:
        print("Not a prime number")


primeNumber(9)

# other method


def primeNumber(x=0):
    count = 0
    if x <= 1:
        print("Not a primenumber")
    else:
        for i in range(2, x):
            if x % i == 0:
                count = count + 1

        if count > 0:
            print(f"{x} is Not a Prime Number")
        else:
            print(f"{x} is a Prime Number")


primeNumber(9)
