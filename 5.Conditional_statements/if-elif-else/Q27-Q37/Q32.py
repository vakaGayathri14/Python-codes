"""
Q32. Ask 4 numbers from user. Make sure all the numbers entered by user
are different. Print which number is the smallest

"""

num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))
num3 = int(input("Enter the 3rd number"))
num4 = int(input("Enter the 4th number"))

if num1<num2 and num1<num3 and  num1<num4:
    print("num1 is the smallest")
elif num2<num1 and num2<num3 and  num2<num4:
    print("num2 is the smallest")
elif num3<num1 and num3<num2 and  num3<num4:
    print("num3 is the smallest")
elif num4<num1 and num4<num1 and  num4<num3:
    print("num4 is the smallest")
else:
    print("Invalid number")