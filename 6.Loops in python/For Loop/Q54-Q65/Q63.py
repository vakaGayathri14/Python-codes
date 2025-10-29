"""Q63. Ask a number from user. Print the multiplication table of that number."""

n = int(input("Enter the table you want to learn: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")