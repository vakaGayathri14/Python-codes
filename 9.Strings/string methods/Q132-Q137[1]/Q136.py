"""
Q136. Count the number of spaces in a string entered by user.
"""

x = " "
print(ord(x))

my_str = input("Enter a string: ")
total_count = 0

for i in my_str:
    ascii = ord(i)
    if ascii == 32:
        total_count += 1
print(total_count)
