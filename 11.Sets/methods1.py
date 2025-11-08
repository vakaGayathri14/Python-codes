my_set = {3, 4, 5, 6, 7}
print(my_set)

# if i want to add 100 in the set then
my_set.add(100)
print(my_set)
my_set.add(7)  # as 7 already present
print(my_set)

# if you want to remove 4
my_set.remove(4)
print(my_set)

my_set.remove(100)
print(my_set)

# if i want to remove 1000 as 1000 not there in the set
my_set.remove(1000)  # I will get error
print(my_set)

