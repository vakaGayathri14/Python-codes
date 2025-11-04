"""
Q95. Make your own list. Print all the elements present at even index
position.

"""

my_list = [51, 74, 85, 91, 52, 44]

for i in range(len(my_list)):
    if i % 2 == 0:
        print(my_list[i])
