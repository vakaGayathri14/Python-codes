"""
Q38. Write a program that takes three numbers as input and determines
the largest one using nested if-else statements. Make sure all 3 numbers
entered by user are dierent
"""
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

if (num1>=0 and num2 >=0 and num3 >=0):
    if(num1>num2 and num1>num3):
        print("num1 is the greatest")
    elif(num2>num1 and num2>num3):
        print("num2 is greatest")
    elif (num3>num1 and num3>num2):
        print("num3 is greatest")
    else:
        print("Invalid")
else:
    print("negative num")