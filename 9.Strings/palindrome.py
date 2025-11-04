"""
palindrome

mom - mom
noon - noon

"""

x = input("Enter a string: ")
y = x[::-1]
if x == y:
    print("palindrome")
else:
    print("not a palindrome")
