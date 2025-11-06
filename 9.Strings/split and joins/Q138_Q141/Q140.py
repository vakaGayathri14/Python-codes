"""
Q140. Write a program that reverses each word in a sentence while
maintaining the word order. For example, "Hello World" should become

"""

my_str = input("Enter a string: ")
words = my_str.split()
print(words)

words = " ".join(i[::-1] for i in words)
print(words)
