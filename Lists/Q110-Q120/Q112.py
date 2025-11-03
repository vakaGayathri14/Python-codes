"""
Q112. Take 10 integer inputs from user and store them in a list. Now, copy
all the elements in another list but in reverse order.

"""

my_list = [5, 1, 10, 20, 5, 1, 1, 9, 3, 4]
print(my_list)
# list2 = my_list.copy()
# list2.reverse()
# print(my_list)
# print(list2)
lst2 = []
for i in range(len(my_list) - 1, -1, -1):
    lst2.append(my_list[i])
print(lst2)
