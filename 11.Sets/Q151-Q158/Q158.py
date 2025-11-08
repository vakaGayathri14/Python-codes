"""
Q158. Ask a string from user, remove all the duplicates from that string and
print that string again (order does’nt matter)

"""

st = input("Enter a string:")
# print(set(st))

new_st = set(st)
x = str(new_st)
print(x, type(x))

z = "".join(new_st)  # one way of doing
y = "".join(i for i in new_st)  # other way
print(y)
print(z)
