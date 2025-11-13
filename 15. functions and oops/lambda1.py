# Take a argument which will be a number
# make a list from 0 to that number using lambda function

make_list = lambda n: [i for i in range(0, n + 1)]
print(make_list(100))

list1 = make_list(5)
print(list1)

# if you want to input from user

make_list = lambda n: [i for i in range(0, n + 1)]
x = int(input("Enter the length: "))

print(make_list(x))
