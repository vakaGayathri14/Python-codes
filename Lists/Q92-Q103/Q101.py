# Q101. Make your own list. Print how many positive and negative numbers are here

my_list = [51, 85, 1748, 44, 52, 100, 200]
positive = 0
negative = 0

for i in my_list:
    if i < 0:
        negative = negative + 1
    elif i >= 0:
        positive = positive + 1
print(negative)
print(positive)
