x = {"name": "Honey", "age": 22, "gender": "female"}
y = {"name": "radha", "age": 36, "gender": "female"}
print(x, type(x))
print(y, type(y))

# in the below i just repeated the key name again then the o/p isthe name value is being assigned by the last value of that key in this case it is muskan if you give different key names then there is no issue
x = {"name": "Honey", "age": 22, "gender": "female", "name": "Muskan"}
print(x)

x = {"name": "Honey", "age": 22, "gender": "female", "Name": "Muskan"}
print(x)

# below i have repeated value 22 again can tht be possible? yes it is
x = {"name": "Honey", "age": 22, "gender": "female", "marks": 22}
print(x)

x = {
    "name": "Honey",
    "age": 22,
    "gender": "female",
    "marks": 22,
}

# my keys can be of int/float/string but not rest but value can be of any data type

x = {
    "name": "Honey",
    "age": 22,
    "gender": "female",
    "marks": 22,
    1: 2,
    2: 3,
}

print(x)

# x = {
#     "name": "Honey",
#     "age": 22,
#     "gender": "female",
#     "marks": 22,
#     1: 2,
#     2: 3,
#     [1, 2, 3]: 4, # not possible
# }
# print(x)

x = {
    "name": "Honey",
    "age": 22,
    "gender": "female",
    "marks": [45, 65, 43, 32, 45],  # accepted
    1: 2,
    2: 3,
}

print(x)
