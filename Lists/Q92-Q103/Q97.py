"""Q97. Make your own list. Count the number of even numbers present in
that list.
"""

my_list = [51, 85, 91.66, 44, 52, 100, 200]
total = 0

for i in my_list:
    if i % 2 == 0:
        total = total + 1
print(total)
