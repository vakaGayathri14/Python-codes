# a = 15


# def change():
#     # Local variable
#     a = 30
#     print(a)


# print(a)
# change()
# print(a)

"""
o/p:
    15
    30
    15

"""

a = 15


def change():
    global a
    a = 30
    print(a)


print(a)
change()
print(a)

"""
o/p:
    15
    30
    15

"""
