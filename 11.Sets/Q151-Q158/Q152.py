"""
Q152. Python program to find common elements in three lists using sets.

"""

a = [1, 2, 3, 4]
b = [4, 3, 5, 2]
c = [5, 1, 2, 0, 9, 4, 5, 7]

d = set(a)
e = set(b)
f = set(c)

print(d)
print(e)
print(f)
x = d.intersection(e)
print(x)
print(f.intersection(x))

# other way

print(d.intersection(e).intersection(f))


# other way
print(set(a) & set(b) & set(c))
