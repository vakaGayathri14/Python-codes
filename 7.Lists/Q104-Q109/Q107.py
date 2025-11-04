"""
Q107. Ask the user for a number. Then, from a list of numbers, remove all
the numbers that can be divided by the number the user entered.

"""

num = int(input("Enter a number"))

my_list = [10, 15, 25, 20, 30]

for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] % num == 0:
        my_list.pop(i)
print(my_list)
