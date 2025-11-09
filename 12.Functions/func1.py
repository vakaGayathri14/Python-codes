def greet():
    print("Hello Coder")


greet()
greet()
greet()

# print even numbers from 1 to 10


def evenNumbers():
    for i in range(1, 11):
        if i % 2 == 0:
            print(i, end=" ")


evenNumbers()


# 2 number addition


def add():
    num1 = 67
    num2 = 13
    print(num1 + num2)


add()
# print(num1) # here I will get error because num1 is not defined
# because num1 is declared inside the function so it is valid only till that function not outside so that is called local variable


def add():
    num1 = 67
    num2 = 13
    print(f"sum -> {num1 + num2}")


num1 = 100
num2 = 100
add()
print(num1) # so now the above num1 = 100 value will print here and also those are stored in different address and the variables declared inside the function will have different address
print(num2)


#user input

def add():
    num1 = int(input("Enter a num1: "))
    num2 = int(input("Enter a num2: "))
    print(f"sum -> {num1 + num2}")

num1 = 100
num2 = 100
add()
print(num1) # so now the above num1 = 100 value will print here and also those are stored in different address and the variables declared inside the function will have different address
print(num2)


#subtract

def sub():
    num1 = int(input("Enter a num1: "))
    num2 = int(input("Enter a num2: "))
    print(f"sub -> {num1 - num2}")
sub()

