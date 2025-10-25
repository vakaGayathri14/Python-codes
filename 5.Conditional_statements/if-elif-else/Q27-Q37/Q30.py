"""
Q30. Write a program to check if the last digit of a number is divisible by 5
or not.
"""
number = input("Enter a number:")
# x = int(number[-1]) 
# print(x,type(x))
# y = x % 5
# print(y,type(x))


if (int(number[-1])%5 ==0):
    print("Divisible by 5")
else:
    print("Not divisible bye 5")