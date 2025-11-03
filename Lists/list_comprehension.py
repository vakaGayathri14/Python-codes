my_list = []
# using for loop
# for i in range(1, 21):
#     my_list.append(i)
# print(my_list)

# using list comprehension
# my_list = [i for i in range(1, 21)]
# print(my_list)

# my_list = [i + 6 for i in range(1, 21)]
# print(my_list)

# my_list = [i for i in range(1, 1001)]
# print(my_list)

# my_list = ["even" for i in range(1, 21)]
# print(my_list)

# my_list = [i % 2 for i in range(1, 21)]
# print(my_list)

"""i=1 ODD
i=2 EVEN

[ODD,EVEN,ODD,EVEN,ODD,EVEN]"""

# new = ["EVEN" if i % 2 == 0 else "ODD" for i in range(1, 7)]
# print(new)


"""
print even numbers list 
"""

even = [i for i in range(1, 10) if i % 2 == 0]
print(even)

# check if a number is divisible by 5

div = [i for i in range(1, 20) if i % 5 == 0]
print(div)


