"""
count, Startswith, Endswith,
Index, Find, Replace, Strip

"""

# count -> checks the repetition of characters and it gives the count of them respectively

my_str = "hello world python is good"
x = my_str.count("h")
y = my_str.count(" ")
z = my_str.count("th")
print(x)
print(y)
print(z)

# startswith and endswith gives o/p in boolean
my_str = "hello world python is good"
x = my_str.startswith("h")
y = my_str.startswith("ll")
z = my_str.startswith("hello")

print(x)
print(y)
print(z)


# endswith

my_str = "hello world python is good"
x = my_str.endswith("h")
y = my_str.endswith("d")
z = my_str.endswith("good")

print(x)
print(y)
print(z)

# index

my_str = "hello world python is good"
x = my_str.index("h")
y = my_str.index("d")
z = my_str.index("good")
# a = my_str.index("z")
# print(a) #error as i don't have z in the string if i do same with find it will give o/p as -1


print(x)
print(y)
print(z)

# find
a = my_str.find("z")
print(a)

# replace h with z
my_str = "hello world python is good"
x = my_str.replace("h", "z")
print(x)

# strip -> it remove by default spaces from starting and ending
my_str = "         hello world                 "
x = my_str.strip()
print(my_str)
print(x)


my_str = "         hello world                 "
x = my_str.strip("@")
print(my_str)
print(x)


my_str = "@@@@@@@@@hello world                 "
x = my_str.strip("@")
print(my_str)
print(x)


my_str = "@@@@@@@@@hello world@@@@@@"
x = my_str.strip("@")
print(my_str)
print(x)
