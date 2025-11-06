"""
Q139. Write a program that accepts a string and capitalizes the first letter
of each word while converting all other letters to lowercase.

"""

my_str = input("Enter a string: ")
x = my_str.title()
print(x)


# other method
my_str = input("Enter a string: ")
words = my_str.split()
result = " ".join(i.capitalize() for i in words)
print(result)
