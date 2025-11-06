"""
Q138. Write a program to reverse the order of words.

EX: My_str = "Hello World"
o/p: World Hello4

EX: My_str = "python is good
o/p: good is python

"""

x = input("Enter a string: ")
y = x.split()
print(y)
z=y[::-1]
print(z)

a=" ".join(z)
print(a)
