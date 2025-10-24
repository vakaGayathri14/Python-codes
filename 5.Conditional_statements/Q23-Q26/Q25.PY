"""
Q25. Write a program that takes two numbers as input and checks if the
first number is divisible by the second
"""

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

if (num1%num2 == 0):
    print(f"first number is divisible by second")
else:
    print(f"first number is not divisible by second")