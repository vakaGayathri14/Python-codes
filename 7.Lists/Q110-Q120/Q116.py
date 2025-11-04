"""
Q116. Write a Python code to find the second largest element in a list
without sorting

"""

my_list = [5, 10, 15, 25, 20, 15]

# using sorting
# my_list.sort()
# my_list.reverse()
# print(my_list[1])


# without sorting
my_list = [54, 32, 17, 67, 43, 11, 87, 44, 54, 32]
largest = float("-inf")
second_largest = float("-inf")


for i in my_list:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i
print(second_largest)
