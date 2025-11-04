"""
Q120. Write a program that swaps the first and last elements of a given list.

"""

x = [32, 10, "Anirudh", 55.90, "xyz"]
print(x)
a = x[0]
x[0] = x[-1]
x[-1] = a
print(x)


# other method only works for numeric values
x[0] = x[0] + x[-1]
x[-1] = x[0] - x[-1]
x[0] = x[0] - x[-1]

print(x)


# other approach only supports for numeric

x[0] = x[0] ^ x[-1]
x[-1] = x[0] ^ x[-1]
x[0] = x[0] ^ x[-1]

print(x)

# if we want to swap a number and a string then usetuple unpacking

x = [32, 10, "Anirudh", 55.90, "xyz"]
x[0], x[-1] = x[-1], x[0]
print(x)
