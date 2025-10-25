"""
Q27. Write a program to check if the number is ODD, EVEN or Equal to Zero
"""

num = int(input("Enter a number: "))

if (num == 0):
    print("num is equal to zero")
elif (num%2 == 0):
    print("Even number")
else:
    print("odd number")