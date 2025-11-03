"""
Q114. Write a Python code to find the occurrence of each element in a list
and print the element with the highest occurrence.
"""

my_list = [5, 10, 15, 25, 20, 15, 5, 2, 5, 5]

for i in range(len(my_list)):
    x = my_list.count(my_list[i])
print(f"{my_list[i],x}")
