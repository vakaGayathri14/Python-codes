"""
Q168. Write a function that takes three numbers as parameters and prints
the largest among them.

"""


# method 1
def largestNumber1(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1}  1 is the largest")
    elif num2 > num1 and num2 > num3:
        print(f"{num2}  2 is the largest")
    else:
        print(f"{num3}  3 is the largest")

largestNumber1(10, 100, 2)
largestNumber1(10, 10, 10)


# def largestNumber(num1, num2, num3):
#     result = num1
#     for i in [num1, num2, num3]:
#         if i > result:
#             result = i
#     print(f"Largest Number is {result}")


# largestNumber(103, 40, 80)
