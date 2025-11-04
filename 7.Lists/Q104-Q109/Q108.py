"""
Q108. Generate a list of at least 10 numbers. Then, create two separate
lists called 'odd' and 'even.' Put all the odd numbers from the original list
into the 'odd' list, and all the even numbers into the 'even' list.
Q109. Start by creating two separate lists with random numbers. Then,
create a third list that merges the numbers from the first and second lists
together.
"""

my_list = [3, 8, 12, 17, 22, 30, 35, 41, 48, 50]
odd = []
even = []

for i in my_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)
