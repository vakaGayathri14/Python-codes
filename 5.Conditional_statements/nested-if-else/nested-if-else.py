"""
A number is positive, negative, zero
"""

num = int(input("Enter a number: "))
if num>=0:
    if num>0:
        print("positive")
    else:
        print("zero")
else:
    print("negative")

# //other approach 

if num>0:
    print("positive")
else:
    if num ==0:
        print("zero")
    else:
        print("negative")
