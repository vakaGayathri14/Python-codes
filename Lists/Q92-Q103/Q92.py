"""
Q92. Make your own list. Print the list in reverse

"""

my_list = [4, -98, "hello", 22.22, 100]

for i in range(0, len(my_list)):
    print(my_list[i], end=" ")
print()
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i], end=" ")
