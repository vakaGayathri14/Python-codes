"""
Q111. Make a list. Then ask a number from user. If number exists in that list
then print the position of the element else print -1
"""

# my_list = [5, 1, 5, 10, 20, 5, 1, 1]
# n = int(input("enter a number"))
# for i in range(len(my_list)):
#     if my_list[i] == n:
#         x = my_list.index(n)
#         print(x)
#     else:
#         print("-1")
# print(x)

# other approach

my_list = [5, 1, 5, 10, 20, 5, 1, 1]
n = int(input("Enter a number: "))

if n in my_list:
    index = my_list.index(n)
    print(index)
