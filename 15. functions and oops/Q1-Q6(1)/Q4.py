"""
write a python function that takes a number as a parameter and checks wheather the number is prime or not.

"""


def is_prime(num):
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors = factors + 1

    if factors == 2:
        return "prime number"
    else:
        return "not prime number"


x = int(input("Enter a number: "))
print(is_prime(x))
