# Q102. Make your own list.Print the largest number present in that list.

my_list = [51, 85, 1748, 44, 52, -100, 200]

largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i
print(largest)
