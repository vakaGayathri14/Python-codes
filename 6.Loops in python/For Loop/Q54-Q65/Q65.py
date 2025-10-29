"""Q65. Ask to numbers x and y from the user. If x<y then print all the
numbers from x to y, but if y<x then print all the numbers from y to x."""

x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))

if x<y:
    for i in range(x,y+1,1):
        print(i)
else:
    for i in range(y,x+1,1):
        print(i)
