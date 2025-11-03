"""
Q110. Make a list of your own. And remove all the duplicates element from
that list.
"""

my_list = [5, 1, "code and debug", 5, 10, 20, 5, 1, 1]
for i in range(len(my_list) - 1, -1, -1):
    if my_list.count(my_list[i]) > 1:
        my_list.pop(i)
print(my_list)
