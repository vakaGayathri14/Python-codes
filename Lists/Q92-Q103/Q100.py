# Q100. Make your own list. Find the sum of all numbers divisible by 3 or 4

my_list = [51, 85, 1748, 44, 52, 100, 200]
total = 0

for i in my_list:
    if i % 3 == 0 or i % 4 == 0:
        total = total + i
print(total)
