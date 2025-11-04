"""
Q130. Ask start and end index from the user. Create a list from start index
to end index using slicing.
"""

start = int(input("Enter the start number"))
end = int(input("Enter the end number"))

a = [23, 54, 78, 43, 12, 34, 89]
b = a[start : end + 1]

print(b)
