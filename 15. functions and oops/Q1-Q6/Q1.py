"""
1.write a python function to reverse a string using slicing and return it.

"""


def rev(st):
    r = st[::-1]
    if st == r:
        return r
    else:
        return "not possible"


print(rev("MOM"))
