my_set = {1, 2, 3, 4, 5, 6, 7, 8}

# my approach
num = int(input("Enter a number:"))
if num in my_set:
    print("True")
else:
    print("False")

# other way
found = False
for i in my_set:
    if i == num:
        found = True
if found:
    print("YES")
else:
    print("No")
