a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8, 9]

# find out what are all the common elements from the list

c = set(a)
d = set(b)

# print(c.intersection(d))

result = c.intersection(d)
print(result)

e = list(result)
print(e)
