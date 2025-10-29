"""
Q52. Calculate factorial of a number entered by user.
"""

num = int(input("Enter a number:"))
total = 1
while num>=1:
    total = total * num
    num = num-1
print(total)


