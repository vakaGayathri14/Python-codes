"""
Q104. Write a program that prompts the user to specify the length of a list
and then requests numbers to populate that list. Display the final list as
the output.

"""
# using for loop
x = int(input("Enter the length of a list: "))
result = []
for i in range(0, x):
    y = int(input("Enter a number: "))
    result.append(y)
print(result)

# using while loop
x = int(input("Enter the length of a list: "))
res = []
i = 1
while i <= x:
    y = int(input(f"Enter a number at position {i} : "))
    res.append(y)
    i += 1
print(res)
