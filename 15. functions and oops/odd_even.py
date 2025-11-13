# # if a number is even return true else return false
check_even = lambda n: n % 2 == 0
if check_even(100):
    print("Even")
else:
    print("Odd")

# # other way
lambda n: print("Even") if n % 2 == 0 else print("Odd")

# using list comprehension

y = int(input("Enter the number: "))
x = ["Even" if i % 2 == 0 else "odd" for i in range(1, y + 1)]
print(x)

# other way

y = int(input("Enter the number: "))
x = ["Even" if y % 2 == 0 else "odd"]
print(x)
