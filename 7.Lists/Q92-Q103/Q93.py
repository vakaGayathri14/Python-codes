"""
Q93. Make your own list. Print all the even numbers present in the list.
"""

my_list = [51, 74, 85, 91, 52, 44]
for i in my_list:
    if i % 2 == 0:
        print(i, end=" ")
