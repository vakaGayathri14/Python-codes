"""
Q164. Write a Python program to find elements in a given set that are not
in another set.
"""

set1 = {5, 6, 2, 1, "Honey"}
set2 = {"python", 76, 22, 91, -991}

if set1 in set2:
    print("elements in set1 are in set2")
else:
    print("elements in one set are not there in set2")
