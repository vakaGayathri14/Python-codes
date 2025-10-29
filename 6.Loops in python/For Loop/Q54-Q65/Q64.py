# Calculate factorial of a number entered by user

n = int(input("Enter a number: "))

prod =1
for i in range(n,0,-1):
    prod = prod *i
print(prod)
