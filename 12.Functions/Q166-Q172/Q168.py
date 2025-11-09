"""
Q168. Write a function that takes three numbers as parameters and prints
the largest among them.

"""


def largestNumber(num1, num2, num3):
    result = num1
    for i in [num1, num2, num3]:
        if i > result:
            result = i
    print(f"Largest Number is {result}")


largestNumber(103, 40, 80)
