my_set = {}
print(my_set)
print(type(my_set))  # as it is empty list it shows the type as dictionary

# to overcome the above case use the below way
my_set = set()
print(my_set)
print(type(my_set))


# now if i want to add something in empty set
my_set.add(1)
my_set.add(100)
print(my_set)

# if i want to add multiple elements inthe set then
my_set.update([1, 2, 3, 4, 5, 4, 2, 1, 5])
print(my_set)
