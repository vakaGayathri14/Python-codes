# scoping: if we create a variable inside a function that is valid only to that function if it goes outside it will give an error


def addition():
    num1 = int(input("Enter num 1 = "))
    num2 = int(input("Enter num 2 = "))
    print(f"ans = {num1 + num2}")


addition()
addition()
# print(num1) error because num1 is declared inside that function
