# if you want to add an element in tuple then convert in to list and then back to tuple

my_tuple = (56, 87, 74, 41, 52)

my_list = list(my_tuple)
print(my_list)

my_list.append(100)
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
