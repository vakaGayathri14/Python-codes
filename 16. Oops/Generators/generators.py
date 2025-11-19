# # generators: It will give value one by one how it gives values using yield


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for i in numbers():
    print(i)


for i in range(1, 11):  # here range also do yield
    print(i)


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


x = numbers()
print(x)  # here generator object will be created
print(next(x))  # here next will print the next value
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print("---------------")
for i in numbers():
    print(i)
