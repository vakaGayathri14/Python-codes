# Q103. Make your own list. Print the smallest number present in that list

my_list = [51, 85, 1748, 44, 52, -100, -200]
smallest = my_list[0]

for i in my_list:
    if i < smallest:
        smallest = i
print(smallest)
