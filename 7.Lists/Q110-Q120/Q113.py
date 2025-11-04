"""
Q113. Write a program to find the average of all the numbers present in the
list

"""

my_list = [5, 10, 15, 25, 20, 15]
print(len(my_list))
avg = 0
for i in my_list:
    avg = avg + i
total = avg / len(my_list)
print(avg)
print(f"average is {total}")
