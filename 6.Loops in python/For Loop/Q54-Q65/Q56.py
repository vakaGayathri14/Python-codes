"""Q56. Ask start number and end number from user. Print all the numbers
from start to end using while loop"""

Start_num = int(input("Enter the starting number"))
end_num = int(input("Enter the ending number"))

for i in range(Start_num,end_num+1):
    print(i)