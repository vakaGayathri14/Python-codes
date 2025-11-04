"""
Q127. Implement a python program to split a list into two equal parts using
slicing. One list should contain 1st half and another list should contain 2nd
half.

"""

a = [10, 20, 30, 40, 50, 60, 70, 80, 90]

y = a[: len(a) // 2]
print(y)
z = a[len(a) // 2 :]
print(z)
