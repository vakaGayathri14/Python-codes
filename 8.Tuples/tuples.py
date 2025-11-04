# Tuple is immutable you cannot add or delete or update
my_tuple = (56, 87, 74, 41, 52)

print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])

# my_tuple[0] = 100
# print(my_tuple)

# In tuple you can use 2 methods count & Index

x = my_tuple.count(87)
print(x)

y = my_tuple.index(87)
print(y)

for i in my_tuple:
    print(i)
