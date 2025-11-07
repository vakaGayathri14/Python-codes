# Q144. Write a Python program to sum all the items in a dictionary.

my_dict = {"age": 22, "Class": 10, "section": 20}

total = 0
for v in my_dict.values():
    total = total + v
print(total)


# 2nd method

print(my_dict.values())
print(list(my_dict.values()))
print(sum(list(my_dict.values())))
