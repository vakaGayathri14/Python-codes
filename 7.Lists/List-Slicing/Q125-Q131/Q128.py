"""
Q128. Implement a python program to get the last 'n' elements from a list
using slicing.
"""

a = [23, 54, 78, 43, 12, 34, 89]
n = int(input("enter the value"))
b = a[-n::]
print(b)
