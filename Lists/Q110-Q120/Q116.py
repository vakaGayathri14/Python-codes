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
new = 0
largest = []
for i in range(len(my_list)):
    if my_list[i] > new:
        largest = my_list.append(my_list[i])
print(largest)
