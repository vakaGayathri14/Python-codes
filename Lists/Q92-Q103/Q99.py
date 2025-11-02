"""Q99. Make your own list. Find the sum of all even numbers present in that
list.
"""

my_list = [51, 85, 1748, 44, 52, 100, 200]

total = 0

for i in my_list:
    if i % 2 == 0:
        total = total + i
print(total)
