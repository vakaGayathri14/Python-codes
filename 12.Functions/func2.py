# using paramters
def add(a, b):
    print(a + b)


add(11, 23)
add(100, 200)
# add()  # In this case will get error because we haven't passed the arguments
# add(100, 200,300)# In this case will get error because we have to give only 2 arguments but here we have provided 3
add("Hi", "Hello")


# If i want to take user input
def add1(a, b):
    print(a + b)


x = int(input("Enter a value: "))
y = int(input("Enter another value: "))

add1(x, y)
