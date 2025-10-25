"""
Q36. Take three numbers as input from User and print which one is greater
or are they equal.
"""

num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))
num3 = int(input("Enter the 3rd number"))

if (num1>num2 and num1>num3):
    print("num1 is the greatest")
if (num2>num1 and num2>num3):
    print("num1 is the greatest")
if (num3>num1 and num3>num1):
    print("num3 is the greatest")
else:
    print("none")