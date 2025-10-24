"""
Q14. Write a Python program to calculate the compound interest for a
given principal, rate of interest, and time period. Ask everything from the
user.

"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in %): "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

amount = principal * (1+(rate/(100*n))) ** (n * time)
compound = amount - principal

print(f"amount: {amount}")
print(f"compound: {compound}")