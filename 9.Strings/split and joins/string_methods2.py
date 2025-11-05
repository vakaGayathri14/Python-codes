# split

a = "hello world this is python"
words = a.split()
print(words)

b = "hello-world-this-is-python"
words1 = b.split()
print(words1)

c = "hello-world-this-is-python"
words2 = c.split("-")
print(words2)


# Join -> combining of elemnts from a list to string in this case you can only combine strings not list
my_list = ["abc", "xyz", "hello", "honey"]
my_string = " ".join(my_list)
print(my_string)
print(type(my_string))

my_list = ["abc", "xyz", "hello", "honey"]
my_string = "-".join(my_list)
print(my_string)
print(type(my_string))

my_list = ["abc", "xyz", "hello", "honey"]
my_string = " | ".join(my_list)
print(my_string)
print(type(my_string))

# In this case i got error because for join we should have only strings but not integer
# my_list = ["abc", "xyz", "hello", "honey", 56]
# my_string = " | ".join(my_list)
# print(my_string)
# print(type(my_string))

# Another way we can also use joins using list comprehension
my_list = ["abc", "xyz", "hello", "honey"]
my_string = " ".join(i for i in my_list)
print(my_string)
print(type(my_string))

# error due to integer
# my_list = ["abc", "xyz", "hello", "honey", 56]
# my_string = " ".join(i for i in my_list)
# print(my_string)
# print(type(my_string))

# type caste to str
my_list = ["abc", "xyz", "hello", "honey", 56]
my_string = " ".join(str(i) for i in my_list)
print(my_string)
print(type(my_string))


# reverse
my_list = ["abc", "xyz", "hello", "honey", 56]
my_string = " ".join(str(i)[::-1] for i in my_list)
print(my_string)
print(type(my_string))
