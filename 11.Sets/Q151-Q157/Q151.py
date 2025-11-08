"""
Q151. Given two lists a, b. Check if two lists have at least one element
common in them.

"""

a = [1, 2, 3, 4]
b = [4, 3, 5, 2]

c = set(a)
d = set(b)
print(c)
print(d)

print(c.intersection(d))
