"""
Q123. Generate a list of strings where each string repeats itself three times,
using list comprehension.

"""

x = ["a", "b", "c"]
z = ["xyz", "zz", "ab"]

y = [i * 3 for i in z]
print(y)
