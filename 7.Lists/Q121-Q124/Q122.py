"""
Q122. Given a list of strings, create a new list containing the lengths of
each string using list comprehension.
"""

y = ["done", "python", "", "ok bye"]
x = [len(y[i]) for i in range(0, 4)]
print(x)
