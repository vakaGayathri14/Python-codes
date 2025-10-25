"""
Q40. Create a program that calculates the price of a movie ticket based on
the age of the customer. If the customer is under 12, the ticket costs $5; if
they are between 12 and 65, the ticket costs $10; otherwise, it's $7
"""
age = int(input("Enter your age"))

if age>=0:
    if age<12:
        print("price is $5")
    elif (age>=12 and age<=65):
        print("price is $10")
    else:
        print("price is $7")
else:
    print("no ticket")
    

