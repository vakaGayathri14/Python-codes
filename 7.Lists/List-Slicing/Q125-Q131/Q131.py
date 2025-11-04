"""
Q131. Ask ‘n’ from user. Create a list of first n elements but in reverse order
using slicing.
"""

a = [23, 54, 78, 43, 12, 34, 89]
n = int(input("Enter a number: "))

b = a[:n][::-1]
print(b)
