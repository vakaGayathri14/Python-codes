"""
Q53. Ask to numbers x and y from the user. If x<y then print all the
numbers from x to y, but if y<x then print all the numbers from y to x.
"""

x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))

while x<y:
    print(x)
    x = x+1
while y<x:
    print(y)
    y=y+1

    

