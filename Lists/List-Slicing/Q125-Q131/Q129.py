"""
Q129. Ask ‘n’ from user. Create a list of last n elements but in reverse order
using slicing.
"""

n = int(input("Enter a number"))
X = []
for i in range(n):
    X.append(i)
    z = X[::-1]
print(X)
print(z)
