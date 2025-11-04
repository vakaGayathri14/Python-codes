a = [59, 68, 100, 5, "honey", True, 55.556, "code"]
print(59 in a)
print("honey" in a)
print(105 in a)
print(105 not in a)


# ask number from user you have to print yes if that number exists in list else no
num = int(input("Enter a number: "))
lst1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if num in lst1:
    print("yes")
else:
    print("no")

# other way
if lst1.count(num) > 0:
    print("yes")
else:
    print("no")
