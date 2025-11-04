"""
Q117. Make a program that takes a list of integers and returns the product
of all the elements.
"""

# my_list = [5, 10, 15, 25, 20, 15]
# prod = 1
# for i in my_list:
#     prod = prod * i
# print(prod)

len_list = int(input("Enter the length of the list"))
lst1 = []
prod = 1

for i in range(len_list):
    x = int(input("Enter the number: "))
    lst1.append(x)
    prod = prod * lst1[i]
print(lst1)
print(prod)
