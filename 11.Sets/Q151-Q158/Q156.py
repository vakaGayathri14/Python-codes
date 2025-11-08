"""
Q156. Write a Python program to check if two given sets have no elements
in common.
"""

set1 = {5, 6, 2, 1, "Honey"}
set2 = {"python", 76, 22, 91, -991}

# result = set1 & set2
result = set1.intersection(set2)
print(result)
print(len(result))

if len(result) == 0:
    print("Both sets have nothing in common")
else:
    print(f"sets have {result} in common ")

# other method
