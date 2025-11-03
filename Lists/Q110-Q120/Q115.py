"""
Q115. Write a program that has two lists and make a new list that contains
only the common elements between them without duplicates.

"""

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)
