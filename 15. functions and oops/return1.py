# def addition(num1, num2):
#     total = num1 + num2
#     return total


# addition(10, 20)
# If we run the above code we don't get any output


# now i will use return to store now here the return total that total value will store in x and that will be printed
def addition(num1, num2):
    total = num1 + num2
    return total


x = addition(10, 20)
print(x)


# differenceb/w print and return nothing and also other method
def addition(num1, num2):
    total = num1 + num2
    return total


print(addition(100, 200)) # rather than storing it in value you can directly print it using this

# The above process only works only if something returns

# print is used rather than return , here why did you get None because there is nothing to return so None, if didn't get some value then by default it stores as None

def addition(num1, num2):
    total = num1 + num2
    print(total) # 30


x = addition(10, 20) # None
print(x)







