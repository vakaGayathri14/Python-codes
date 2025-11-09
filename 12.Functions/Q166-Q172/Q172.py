"""
Q172. Write a function that takes a string and prints whether it is a
palindrome.

"""


def palindrome(st):
    x = st[::-1]
    if st == x:
        print("Palindrome")
    else:
        print("Not a palindrome")


palindrome("12121y")
