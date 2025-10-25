"""
Q31. Write a program to calculate bill. Ask the final bill_amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final bill_amount to be paid.

Example 1
Enter bill bill_amount = 80000
You got 30% discount
Your final bill is Rs. 56000

"""

bill_amount = int(input("Enter the total bill_amount: "))

if (bill_amount>=50000):
    print(f"Discount is 30 % then final bill_amount to be paid is {bill_amount -(bill_amount * (30/100))}" )
elif (bill_amount>= 40000 and bill_amount <=49999):
    print(f"Discount is 25% then the final bill_amount to be paid is {bill_amount - (bill_amount * (25/100))}")
elif(bill_amount>=30000 and bill_amount<=39999):
    print(f"Discount is 20% then the final bill_amount to be paid is {bill_amount - (bill_amount * (20/100))}")
elif (bill_amount >10000 and bill_amount<=29999):
    print(f"Discount is 10% then the final bill_amount to be paid is {bill_amount - (bill_amount * (10/100))}")
elif(bill_amount>1 and bill_amount<9999):
    print(f"no discount")
else:
    print("No offers currently available")