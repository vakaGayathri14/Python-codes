# Q145. Write a Python program to multiply all the items in a dictionary.

my_dict = {"age": 22, "Class": 10, "section": 20}

mul = 1

for v in my_dict.values():
    mul = mul * v
print(mul)
