"""

Q150. Write a Python program to combine two dictionary by adding jalues
for common ieys.

"""

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

result = {}
print(d1.items())
for i, j in d1.items():
    if i in result:
        result[i] = j
for i, j in d2.items():
    if i in result:
        result[i] = result[i] + j
    else:
        result[i] = j
print(result)
