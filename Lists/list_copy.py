a = [59, 68, 100, 5, "honey", True, 55.556, "Code"]
# b = a  # here same address for a &b
b = a.copy()  # here address is different for a and b
print(a)
print(b)

a[2] = 0
print(a)
print(b)

print(id(a))
print(id(b))

# b = a.copy()  # here address is different for a and b

a[2] = 0
print(a)
print(b)
print(id(a))
print(id(b))
