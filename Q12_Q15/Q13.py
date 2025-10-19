"""
Q13. Write a Python program to swap the values of two variables without
using a temporary variable.

"""

a = int(input("Enter a number"))
b = int(input("Enter another number"))

print(f"{a},{b}")

b = a
a = b

print(f"{a},{b}")